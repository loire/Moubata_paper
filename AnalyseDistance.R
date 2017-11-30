require(tidyr)
require(dplyr)
require(ggplot2)

data = read.table("RES_All_data_close.txt",header=F)

glimpse(data)
colnames(data) = c("QueryID","SubjectID","BlastPerc","BlastAligLength","BlastMimatch","BlastGapOpen","BlastQstart","BlastQend","BlastSstart","BlastSend","BlastEval","BlastBitscore","dnadistF80","Subject_2","dn","ds","vdn","vds","dnds","BlastPerc2","Subject3","Querylength","Subjectlength","homologSpecies")

data %>% ggplot()  + geom_histogram(aes(x=dnadistF80,fill=dnds)) + facet_grid(~ homologSpecies) + theme_bw()
ggsave("plot_DNADist.pdf")

data %>% filter(dnds<5)  %>% ggplot() + geom_point(aes(x=dnadistF80,y=dnds)) + facet_grid(~ homologSpecies) + theme_bw()
ggsave("plot_dist_vs_dnds.pdf")






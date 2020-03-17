#Inputs needed:
#1 No of K
#2 Q file
#3 Single column file containing breed names. No. of rows should be equal to those in the Q file.
#4 ID of your breed
library(tidyverse)
setwd("~/Desktop/Imputation2/desiplus2093/admixture/admixall")

#Get your breeds' Q averages
K <- 9                                            #1
qfile <- read.table("ghurrahplus2093cleanLD.9.Q") #2
idfile <- read.table("tmp")                       #3
colnames(idfile) <- "ID"
qfile <- cbind(idfile,qfile)
mybreedq <- qfile %>% filter(ID == "D")           #4
mybreedqavg <- mybreedq %>% group_by(ID) %>% summarize_all(list(mean))
mybreedqavg <- as.data.frame(t(mybreedqavg[,-1]))
colnames(mybreedqavg) <- "Mybreed"
mybreedqavg <- mybreedqavg %>% mutate(Cluster = rownames(mybreedqavg)) %>% select(Cluster,Mybreed) %>% arrange(desc(Mybreed))

#Get top breeds for each cluster

return_id <- function(column) {
  qfile[which.max(qfile[,column]),1]
}
mybreedqavg <- mybreedqavg %>% mutate(topbreeds = (sapply(Cluster,return_id)))
view(mybreedqavg)

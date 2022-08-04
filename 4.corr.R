#http://www.sthda.com/english/wiki/correlation-matrix-a-quick-start-guide-to-analyze-format-and-visualize-a-correlation-matrix-using-r-software
library("Hmisc")
#file <- "total_variantnorm.csv"
file <- "annotation.csv"
data <- read.table(file,sep=",",header=TRUE,row.names=1,quote = "", stringsAsFactors = FALSE)
data_t <- t(data)


res2 <- rcorr(data_t)

name <- unlist(strsplit(file, split='.', fixed=TRUE))[1]

r <- round(res2$r,2)
<<<<<<< HEAD
r_filtered <-`[<-`(r, lower.tri(r,diag=TRUE), NA)
p <- round(res2$P,2)
p_filtered <-`[<-`(p, lower.tri(p,diag=TRUE), NA)
#write.csv(r_filtered ,paste("corr_",name,".csv",sep=""),row.names=TRUE)
#write.csv(p_filtered,paste("P_",name,".csv",sep=""),row.names=TRUE)


n <- 1:length(p_filtered)#all indexes
n <- n[! n %in% which(p_filtered<=0.05)]#picks indexes which p-values is not <=0.05
filtered_table <-'[<-'(r_filtered,n,NA)#sets these values as NA
write.csv(filtered_table,paste("filtered_r_",name,".csv",sep=""),row.names=TRUE)

=======
r_filtered <-`[<-`(r, lower.tri(r), NA)
p <- round(res2$P,2)
p_filtered <-`[<-`(p, lower.tri(p), NA)
write.csv(r_filtered ,paste("corr_",name,".csv",sep=""),row.names=TRUE)
write.csv(p_filtered,paste("P_",name,".csv",sep=""),row.names=TRUE)
>>>>>>> 73c8aed90d8e3db7034fbc8b7a4d78562bf3704b

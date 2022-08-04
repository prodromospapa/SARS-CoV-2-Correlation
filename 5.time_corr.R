library("Hmisc")
<<<<<<< HEAD
=======
#file <- "total_variantnorm.csv"
>>>>>>> 73c8aed90d8e3db7034fbc8b7a4d78562bf3704b
file <- "annotation.csv"
data <- read.table(file,sep=",",header=TRUE,row.names=1,quote = "", stringsAsFactors = FALSE)

dates <- as.numeric(1:length(names(data)))

<<<<<<< HEAD
corre <- function(x){
return(rcorr(dates,as.numeric(x),type="pearson")$r[2,1])}

p <- function(x){
return(rcorr(dates,as.numeric(x),type="pearson")$P[2,1])}


corr_values <- round(apply(data,1,corre),2)
corr_p_values <- round(apply(data,1,p),2)

merged_table <- do.call(rbind, Map(data.frame, 'Correlation'=corr_values, 'P-values'=corr_p_values))
write.csv(merged_table,'time_corr.csv',row.names=TRUE)
=======
#des gia ta methods poio einai pio swsto kai allakse to [2,1]
corre <- function(x){
return(rcorr(dates,as.numeric(x),type="pearson")$r[2,1])} #https://www.researchgate.net/post/Which-correlation-coefficient-is-better-to-use-Spearman-or-Pearson

p <- function(x){
return(rcorr(dates,as.numeric(x),type="pearson")$P[2,1])} #https://www.researchgate.net/post/Which-correlation-coefficient-is-better-to-use-Spearman-or-Pearson

by_lm <- function(x){
return(lm(x~dates)[[1]][[2]])
}

by_lm_p <- function(x){
return(summary(lm(x~dates))$coefficients[,4][2])
}

corr_values <- apply(data,1,corre)
corr_p_values <- apply(data,1,p)
print(corr_values)
#lm_values <- apply(data,1,by_lm)
#lm_p_values <- apply(data,1,by_lm_p)
#corr_values[which(corr_values[which(p_values < 0.05)] >0)]

name = unlist(strsplit(file, split='.', fixed=TRUE))[1]
write.csv(round(corr_values,2),paste("corrt_",name,".csv",sep=""),row.names=TRUE)
write.csv(round(corr_p_values,2),paste("Pt_",name,".csv",sep=""),row.names=TRUE)
>>>>>>> 73c8aed90d8e3db7034fbc8b7a4d78562bf3704b

country=Germany 

if [ ! -f $country.fasta ] || [ ! -f fasta/${country}01.fasta ]; then
    tar xf msa_*.tar.xz --wildcards 'msa_*/msa_*.fa*' -O | grep -A 1 $country | awk 'length($0)>10'  > $country.fasta
    mkdir -p fasta
    split -l60000 --numeric-suffixes=1 $country.fasta fasta/$country --additional-suffix=.fasta
    rm $country.fasta
fi


#mkdir -p tmp
#path=$(pwd)#gia to tmp
#export MAFFT_TMPDIR="$path/tmp"

mkdir -p mafft
mkdir -p vcf

counter=0
for fasta in fasta/*
do	
	counter=$((counter+1))
	mafft --6merpair --thread -12 --keeplength --addfragments $fasta refseq.fasta > mafft/$country.$counter.mafft.fasta #https://mafft.cbrc.jp/alignment/software/closelyrelatedviralgenomes.html
  #mafft --thread -12 --add $fasta refseq.fasta > mafft/$country.$counter.mafft.fasta #https://bit.ly/3v7MKyQ
	snp-sites mafft/$country.$counter.mafft.fasta -v > vcf/$country.$counter.vcf 
	#gia vcf:
	#ALT: *=deletion 
	#noumera shmainoun 0=ref kai apo ekei kai meta afto pou deixnei to ALT (p.x. 1= prwth thesh) 
done
rm -d tmp
rm -r fasta
rm -r mafft
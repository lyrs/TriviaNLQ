DDIR=data/monument_600
MDIR=output/models/fairseq_fconv_wmt_en_de
RDIR=results/result

if [ -n "$1" ]
    then DDIR=$1
fi

if [ -n "$2" ]
    then MDIR=$2
fi

if [ -n "$3" ]
then 
    RDIR=$3
    if ! [ -e $RDIR ]
    then mkdir -p $RDIR
    fi
fi

fairseq-generate $DDIR/fairseq-data-bin \
--gen-subset train \
--path $MDIR/checkpoint_last.pt \
--beam 5 > $RDIR/train_output.txt

python3 fairseq_output_reader.py $RDIR/train_output.txt > $RDIR/train_translation.sparql

fairseq-generate $DDIR/fairseq-data-bin \
--gen-subset valid \
--path $MDIR/checkpoint_best.pt \
--beam 5 > $RDIR/dev_output.txt

python3 fairseq_output_reader.py $RDIR/dev_output.txt > $RDIR/dev_translation.sparql

fairseq-generate $DDIR/fairseq-data-bin \
--gen-subset test \
--path $MDIR/checkpoint_best.pt \
--beam 5 > $RDIR/test_output.txt

python3 fairseq_output_reader.py $RDIR/test_output.txt > $RDIR/test_translation.sparql

# Query and Analyze
# python3 generate.py $DDIR $RDIR
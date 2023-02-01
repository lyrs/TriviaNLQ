
# Generate dataset for fairseq framework
fairseq-preprocess -s en -t sparql --trainpref $1/train --validpref $1/dev --testpref $1/test --destdir $1/fairseq-data-bin --joined-dictionary
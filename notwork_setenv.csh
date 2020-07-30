setenv KALDI_ROOT /home/fuqiang_luo/H/source/kaldi
[ -f $KALDI_ROOT/tools/env.sh ] && . $KALDI_ROOT/tools/env.sh
setenv PATH $PWD/utils/:$KALDI_ROOT/tools/openfst/bin:$KALDI_ROOT/tools/irstlm/bin/:$PWD:$PATH
source $KALDI_ROOT/tools/config/common_path.sh
setenv LC_ALL C

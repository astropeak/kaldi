for test in dev_clean test_clean dev_other test_other; do for lm in fglarge tglarge tgmed tgsmall; do grep WER exp/tri5b/decode_${lm}_${test}/wer* | utils/best_wer.sh; done; echo; done
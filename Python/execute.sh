temp_path=$(realpath $0)
path=${temp_path%/*}
/usr/hdp/2.6.5.0-292/spark2/bin/spark-submit --master yarn --driver-memory 20G --executor-memory 10G --num-executors 10 --executor-cores 4 $path/solution.py all all



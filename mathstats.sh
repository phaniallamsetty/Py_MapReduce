#!/bin/bash
hadoop jar $HADOOP_INSTALL/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -input $1 -output $2 -file math_map.py math_reduce.py -mapper math_map.py -reducer math_reduce.py

```dataview
table WITHOUT ID file.link AS "标题", dateformat(file.mtime, "yyyy-MM-dd HH:MM") as "时间"
from "40-Research/论文笔记/DeepLearning"
where !contains(file.name,"LUT")
sort file.name
```

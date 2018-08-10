# Project-Overlay-Data-Process


## Rationale
The Project Overlay is an experimental new method of navigating through the GCTools. It encourages navigation of key themes and the groups that contribute to them through a primarily visual medium. The objective is to highlight groups on the GCTools that are doing cool things in key areas.

## Structure

![Data Graphic Model](https://github.com/Lavoiec/Project-Overlay-Data-Process/blob/master/Data%20Graphic%20Model.png)
Whether it is in network graph mode or dendrogram node, the structure of the Project Overlay Data is the same. There are two broad categories that represent different perspectives of the data app: The Communities node and the Issues node. Each node leads to sub-nodes that further break down the theme into its various categories. Jutting from these sub-nodes are the actual groups that are deemed to be related to a specific category. Each of the groups have “Similar Groups” located in the graph, which are determined by the percentage of similar group members.
Each group also has a “Top Contributors” section, which measures the top contributors of “content” (defined as any files, blogs, discussion, bookmarks, polls, photos, etc.) within the group.


 ## Flow
 ![Program Diagram](https://github.com/Lavoiec/Project-Overlay-Data-Process/blob/master/Program%20Diagram.png)

Above is a diagram of the interactions between the data and the files. The flow of the main script follows that of the blue boxes, with each script being run in sequence. The scripts depend on having initial files that are created from a separate process

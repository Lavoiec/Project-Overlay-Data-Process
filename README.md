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

## Group Identification
The structure of the eventual data file is shown in the Structure section; however, it is not yet indicated how groups are determined to be a part of a Community or a Mandate. The method of determination differs for each one respectively. Groups that are linked to Communities are tagged with the most popular tags under the Communities tab, while groups linked to Mandate Letters use Natural Language Processing to match descriptions of groups to descriptions of mandate letters.

*Communities* 

Communities are derived directly from the “Communities” Tab in GCconnex. They consist of fifteen categories derived from https://www.csps-efpc.gc.ca/special_devel-eng.aspx plus an “All Public Service” category. Content created on GCconnex can be given one of these “Communties” tags which guarantees that it will be displayed under the Feed that corresponds to that category. Groups are chosen based on a combination of recent activity and the frequent use of the most common tags in the functional communities. 
Example:
Consider Group A. If Group A has 3 posts with content $a_1,a_2$  and $a_3$, and each piece of content has a tag the following tags:

<a href="https://www.codecogs.com/eqnedit.php?latex=a_1:\{t_1,t_2,&space;t_3\};a_2:\{t_1\};a_3:&space;\{t_4\}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a_1:\{t_1,t_2,&space;t_3\};a_2:\{t_1\};a_3:&space;\{t_4\}" title="a_1:\{t_1,t_2, t_3\};a_2:\{t_1\};a_3: \{t_4\}" /></a>

And the following communities:
<a href="https://www.codecogs.com/eqnedit.php?latex=a_1:\{c_1&space;\};a_2:\{c_2\};a_3:\{c_1\}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a_1:\{c_1&space;\};a_2:\{c_2\};a_3:\{c_1\}" title="a_1:\{c_1 \};a_2:\{c_2\};a_3:\{c_1\}" /></a>
Then Group A has the tags:

<a href="https://www.codecogs.com/eqnedit.php?latex=t_1,&space;t_2,&space;t_3" target="_blank"><img src="https://latex.codecogs.com/gif.latex?t_1,&space;t_2,&space;t_3" title="t_1, t_2, t_3" /></a>
and the communities:

<a href="https://www.codecogs.com/eqnedit.php?latex=c_1,&space;c_2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?c_1,&space;c_2" title="c_1, c_2" /></a>



For each community, ten of the most frequent tags used are identified. Groups that contain the communities and the most frequent tags are retained as the relevant groups, while the rest of the groups are dropped.


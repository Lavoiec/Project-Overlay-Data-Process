import ProjectOverlayDataProcess as data
import utility_funcs as uf
import pandas as pd
import gcconnex as gc
import code

minimum_group_size = 10

def filter_communities_and_tags(df, communitiesdf, oncols):
    """
    Returns groups that are within the list of groups
    that contain a popular tag in each category
    """
    newdf = df.copy()


    newdf = pd.merge(newdf,communitiesdf, on=oncols)

    group_list = list(newdf.guid.unique())

    content_tag_list = communitiesdf.content_tag.unique()

    #return df.loc[df.guid.isin(group_list) & df.content_tag]
    return newdf

def merge_top_contributors(nestdf, groupbycol, nestcol, newcolname, mergedf ,key):

    contributorsdf = uf.nest_for_json(nestdf, groupbycol, nestcol, newcolname)

    newdf = pd.merge(mergedf, contributorsdf, on=key, how='inner')

    return newdf


def main():
    engine, conn = gc.connect_to_database()
    session, Base = gc.create_session()

    groups = data.get_group_properties(conn)
    groups = groups.loc[groups['size'] >= minimum_group_size,:]

    contributors = data.get_top_contributors(conn, 5)
    comms_and_tags = uf.returning_top_tags(groups, 10)
    
    relevant_groups = merge_top_contributors(
        nestdf=contributors, 
        groupbycol='guid',
        nestcol='user',
        newcolname='top_contributors',
        mergedf=groups, key='guid'
        )

    relevantgroups = filter_communities_and_tags(groups, comms_and_tags, oncols=['content_audience', 'content_tag']).dropna()

    relevantgroups = uf.text_cleaning_pipe(relevantgroups,
                                           cols=['name','description'])



    
    relevantgroups.to_csv("relevantgroups.csv")


if __name__ == "__main__":

    main()
    code.interact(local=locals())


 
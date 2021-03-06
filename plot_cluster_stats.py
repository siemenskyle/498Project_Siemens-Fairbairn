"""
file: 'plot_cluster_stats.py'
authors: David Fairbairn and Kyle Siemens
date: December 2016

Some convenient methods for plotting cluster data.
"""

import pandas as pd
import matplotlib.pyplot as plt

def plot_save_init():
    import os
    if not os.path.isdir('./cluster_characterization'):
        print 'Creating an output directory for the images..'
        os.system('mkdir ./cluster_characterization')

def plot_clusterstats(labeled_vars):
    """ """
    import os
    if not os.path.isdir('./cluster_characterization'):
        print 'Creating an output directory for the images..'
        os.system('mkdir ./cluster_characterization')

    print "Number in cluster 0: ",len(labeled_vars.loc[labeled_vars['LABEL']==0.0])
    print "Number in cluster 1: ",len(labeled_vars.loc[labeled_vars['LABEL']==1.0])
    print "Number in cluster 2: ",len(labeled_vars.loc[labeled_vars['LABEL']==2.0])

    plot_score_diff(labeled_vars)
    plot_pit_count(labeled_vars)
    plot_inning(labeled_vars)
    plot_rbi(labeled_vars)
    plot_balls(labeled_vars)
    plot_outs(labeled_vars)
    plot_team_wins(labeled_vars)
    plot_bat_dest_id(labeled_vars)

    """
    # *********************************
    # ******* SCORE DIFF PLOT *********
    # *********************************
    pd.value_counts(labeled_vars.loc[labeled_vars['LABEL']==0.0]['SCORE_DIFF']).sort_index().plot(label='Cluster 0')
    pd.value_counts(labeled_vars.loc[labeled_vars['LABEL']==1.0]['SCORE_DIFF']).sort_index().plot(label='Cluster 1')
    pd.value_counts(labeled_vars.loc[labeled_vars['LABEL']==2.0]['SCORE_DIFF']).sort_index().plot(label='Cluster 2')
    plt.legend()
    plt.title('Score Difference vs. Cluster')
    plt.xlabel('Score Difference')
    plt.ylabel('Number of Occurrences')
    plt.savefig('./cluster_characterization/cluster_scorediff.png')
    plt.gcf().clear()

    # *********************************
    # ******* PITCH COUNT PLOT ********
    # *********************************
    pd.value_counts(labeled_vars.loc[labeled_vars['LABEL']==0.0]['PIT_COUNT']).sort_index().plot(label='Cluster 0')
    pd.value_counts(labeled_vars.loc[labeled_vars['LABEL']==1.0]['PIT_COUNT']).sort_index().plot(label='Cluster 1')
    pd.value_counts(labeled_vars.loc[labeled_vars['LABEL']==2.0]['PIT_COUNT']).sort_index().plot(label='Cluster 2')
    plt.legend()
    plt.title('Pitch Count vs. Cluster')
    plt.xlabel('Pitch Count')
    plt.ylabel('Number of Occurrences')
    #plt.show()
    plt.savefig('./cluster_characterization/cluster_pitch.png')
    plt.gcf().clear()

    # *********************************
    # ************ INNING *************
    # *********************************
    pd.value_counts(labeled_vars.loc[labeled_vars['LABEL']==0.0]['INN_CT']).sort_index().plot(label='Cluster 0')
    pd.value_counts(labeled_vars.loc[labeled_vars['LABEL']==1.0]['INN_CT']).sort_index().plot(label='Cluster 1')
    pd.value_counts(labeled_vars.loc[labeled_vars['LABEL']==2.0]['INN_CT']).sort_index().plot(label='Cluster 2')
    plt.legend()
    plt.title('Inning vs. Cluster')
    plt.xlabel('Inning')
    plt.ylabel('Number of Occurrences')
    plt.savefig('./cluster_characterization/cluster_inning.png')
    plt.gcf().clear()

    # *********************************
    # ******* RBI COUNT PLOTS *********
    # *********************************
    pd.value_counts(labeled_vars.loc[labeled_vars['LABEL']==0.0]['RBI_CT']).sort_index().plot(kind='bar',label='Cluster 0')
    plt.title('RBI Count Distribution for Cluster 0')
    plt.xlabel('RBI Count')
    plt.ylabel('Number of Occurrences')
    plt.savefig('./cluster_characterization/cluster0_RBI.png')
    plt.gcf().clear()

    pd.value_counts(labeled_vars.loc[labeled_vars['LABEL']==1.0]['RBI_CT']).sort_index().plot(kind='bar',label='Cluster 1')
    plt.title('RBI Count Distribution for Cluster 1')
    plt.xlabel('RBI Count')
    plt.ylabel('Number of Occurrences')
    plt.savefig('./cluster_characterization/cluster1_RBI.png')
    plt.gcf().clear()

    pd.value_counts(labeled_vars.loc[labeled_vars['LABEL']==2.0]['RBI_CT']).sort_index().plot(kind='bar',label='Cluster 2')
    plt.title('RBI Count Distribution for Cluster 2')
    plt.xlabel('RBI Count')
    plt.ylabel('Number of Occurrences')
    plt.savefig('./cluster_characterization/cluster2_RBI.png')
    plt.gcf().clear()

    # *********************************
    # ******* OUTS COUNT PLOTS ********
    # *********************************
    pd.value_counts(labeled_vars.loc[labeled_vars['LABEL']==0.0]['EVENT_OUTS_CT']).sort_index().plot(kind='bar',label='Cluster 0')
    plt.title('Outs Count Distribution for Cluster 0')
    plt.xlabel('Outs Count')
    plt.ylabel('Number of Occurrences')
    plt.savefig('./cluster_characterization/cluster0_OUT.png')
    plt.gcf().clear()

    pd.value_counts(labeled_vars.loc[labeled_vars['LABEL']==1.0]['EVENT_OUTS_CT']).sort_index().plot(kind='bar',label='Cluster 1')
    plt.title('Outs Count Distribution for Cluster 1')
    plt.xlabel('Outs Count')
    plt.ylabel('Number of Occurrences')
    plt.savefig('./cluster_characterization/cluster1_OUT.png')
    plt.gcf().clear()

    pd.value_counts(labeled_vars.loc[labeled_vars['LABEL']==2.0]['EVENT_OUTS_CT']).sort_index().plot(kind='bar',label='Cluster 2')
    plt.title('Outs Count Distribution for Cluster 2')
    plt.xlabel('Outs Count')
    plt.ylabel('Number of Occurrences')
    plt.savefig('./cluster_characterization/cluster2_OUT.png')
    plt.gcf().clear()

    # *********************************
    # ******* BALL COUNT PLOTS ********
    # *********************************
    pd.value_counts(labeled_vars.loc[labeled_vars['LABEL']==0.0]['PA_BALL_CT']).sort_index().plot(kind='bar',label='Cluster 0')
    plt.title('Ball Count Distribution for Cluster 0')
    plt.xlabel('Ball Count')
    plt.ylabel('Number of Occurrences')
    plt.savefig('./cluster_characterization/cluster0_BALL.png')
    plt.gcf().clear()

    pd.value_counts(labeled_vars.loc[labeled_vars['LABEL']==1.0]['PA_BALL_CT']).sort_index().plot(kind='bar',label='Cluster 1')
    plt.title('Ball Count Distribution for Cluster 1')
    plt.xlabel('Ball Count')
    plt.ylabel('Number of Occurrences')
    plt.savefig('./cluster_characterization/cluster1_BALL.png')
    plt.gcf().clear()

    pd.value_counts(labeled_vars.loc[labeled_vars['LABEL']==2.0]['PA_BALL_CT']).sort_index().plot(kind='bar',label='Cluster 2')
    plt.title('Ball Count Distribution for Cluster 2')
    plt.xlabel('Ball Count')
    plt.ylabel('Number of Occurrences')
    plt.savefig('./cluster_characterization/cluster2_BALL.png')
    plt.gcf().clear()

    # *********************************
    # ****** BATTER DESTINATION *******
    # *********************************
    pd.value_counts(labeled_vars.loc[labeled_vars['LABEL']==0.0]['BAT_DEST_ID']).sort_index().plot(kind='bar',label='Cluster 0')
    plt.title('Batter Destination (Base #) for Cluster 0')
    plt.xlabel('Batter Destination (Base #)')
    plt.ylabel('Number of Occurrences')
    plt.savefig('./cluster_characterization/cluster0_BATDEST.png')
    plt.gcf().clear()

    pd.value_counts(labeled_vars.loc[labeled_vars['LABEL']==1.0]['BAT_DEST_ID']).sort_index().plot(kind='bar',label='Cluster 1')
    plt.title('Batter Destination (Base #) for Cluster 1')
    plt.xlabel('Batter Destination (Base #)')
    plt.ylabel('Number of Occurrences')
    plt.savefig('./cluster_characterization/cluster1_BATDEST.png')
    plt.gcf().clear()

    pd.value_counts(labeled_vars.loc[labeled_vars['LABEL']==2.0]['BAT_DEST_ID']).sort_index().plot(kind='bar',label='Cluster 2')
    plt.title('Batter Destination (Base #) for Cluster 2')
    plt.xlabel('Batter Destination (Base #)')
    plt.ylabel('Number of Occurrences')
    plt.savefig('./cluster_characterization/cluster2_BATDEST.png')
    plt.gcf().clear()

    # *********************************
    # ******** WIN/LOSS RATIO *********
    # *********************************
   
    pd.value_counts(labeled_vars.loc[labeled_vars['LABEL']==0.0]['TEAM_WINS']).sort_index().plot(kind='bar',label='Cluster 0')
    plt.title('Win Distribution for Cluster 0')
    plt.xlabel('Loss or Win')
    plt.ylabel('Number of Occurrences')
    plt.savefig('./cluster_characterization/outcomes_cluster0.png')
    plt.gcf().clear()


    pd.value_counts(labeled_vars.loc[labeled_vars['LABEL']==1.0]['TEAM_WINS']).sort_index().plot(kind='bar',label='Cluster 1')
    plt.title('Win Distribution for Cluster 1')
    plt.xlabel('Loss or Win')
    plt.ylabel('Number of Occurrences')
    plt.savefig('./cluster_characterization/outcomes_cluster1.png')
    plt.gcf().clear()


    pd.value_counts(labeled_vars.loc[labeled_vars['LABEL']==2.0]['TEAM_WINS']).sort_index().plot(kind='bar',label='Cluster 2')
    plt.title('Win Distribution for Cluster 2')
    plt.xlabel('Loss or Win')
    plt.ylabel('Number of Occurrences')
    plt.savefig('./cluster_characterization/outcomes_cluster2.png')
    plt.gcf().clear()
    """
   
def plot_bat_dest_id(labeled_vars):
    plot_save_init()
    for i in labeled_vars['LABEL'].unique():
        pd.value_counts(labeled_vars.loc[labeled_vars['LABEL']==float(i)]['BAT_DEST_ID']).sort_index().plot(kind='bar',label='Cluster %s' % str(i))
        plt.title('Batter Destination (Base #) for Cluster %s' % str(i))
        plt.xlabel('Batter Destination (Base #)')
        plt.ylabel('Number of Occurrences')
        plt.savefig('./cluster_characterization/cluster%s_BATDEST.png' % str(i))
        plt.gcf().clear()

def plot_balls(labeled_vars):
    plot_save_init()
    for i in labeled_vars['LABEL'].unique():
        pd.value_counts(labeled_vars.loc[labeled_vars['LABEL']==float(i)]['PA_BALL_CT']).sort_index().plot(kind='bar',label='Cluster %s' % str(i))
        plt.title('Ball Count Distribution for Cluster %s' % str(i))
        plt.xlabel('Ball Count')
        plt.ylabel('Number of Occurrences')
        plt.savefig('./cluster_characterization/cluster%s_BALL.png' % str(i))
        plt.gcf().clear()

def plot_outs(labeled_vars):
    plot_save_init()
    for i in labeled_vars['LABEL'].unique():
        pd.value_counts(labeled_vars.loc[labeled_vars['LABEL']==float(i)]['EVENT_OUTS_CT']).sort_index().plot(kind='bar',label='Cluster %s' % str(i))
        plt.title('Outs Count Distribution for Cluster %s' % str(i))
        plt.xlabel('Outs Count')
        plt.ylabel('Number of Occurrences')
        plt.savefig('./cluster_characterization/cluster%s_OUT.png' % str(i))
        plt.gcf().clear()

def plot_rbi(labeled_vars):
    plot_save_init()
    for i in labeled_vars['LABEL'].unique():
        pd.value_counts(labeled_vars.loc[labeled_vars['LABEL']==float(i)]['RBI_CT']).sort_index().plot(kind='bar',label='Cluster %s' % str(i))
        plt.title('RBI Count Distribution for Cluster %s' % str(i))
        plt.xlabel('RBI Count')
        plt.ylabel('Number of Occurrences')
        plt.savefig('./cluster_characterization/cluster%s_RBI.png' % str(i))
        plt.gcf().clear()

def plot_team_wins(labeled_vars):
    plot_save_init()
    for i in labeled_vars['LABEL'].unique():
        pd.value_counts(labeled_vars.loc[labeled_vars['LABEL']==float(i)]['TEAM_WINS']).sort_index().plot(kind='bar',label='Cluster %s' % str(i))
        plt.title('Win Distribution for Cluster %s' % str(i))
        plt.xlabel('Loss or Win')
        plt.ylabel('Number of Occurrences')
        plt.savefig('./cluster_characterization/outcomes_cluster%s.png' % str(i))
        plt.gcf().clear()

def plot_score_diff(labeled_vars):
    plot_save_init()
    for i in labeled_vars['LABEL'].unique():
        pd.value_counts(labeled_vars.loc[labeled_vars['LABEL']==float(i)]['SCORE_DIFF']).sort_index().plot(label='Cluster %s' % str(i))
    plt.legend()
    plt.title('Score Difference vs. Cluster')
    plt.xlabel('Score Difference')
    plt.ylabel('Number of Occurrences')
    plt.savefig('./cluster_characterization/cluster_scorediff.png')
    plt.gcf().clear()

def plot_pit_count(labeled_vars):
    plot_save_init()
    for i in labeled_vars['LABEL'].unique():
        pd.value_counts(labeled_vars.loc[labeled_vars['LABEL']==float(i)]['PIT_COUNT']).sort_index().plot(label='Cluster %s' % str(i))
    plt.legend()
    plt.title('Pitch Count vs. Cluster')
    plt.xlabel('Pitch Count')
    plt.ylabel('Number of Occurrences')
    plt.savefig('./cluster_characterization/cluster_pitchcount.png')
    plt.gcf().clear()

def plot_inning(labeled_vars):
    plot_save_init()
    for i in labeled_vars['LABEL'].unique():
        pd.value_counts(labeled_vars.loc[labeled_vars['LABEL']==float(i)]['INN_CT']).sort_index().plot(label='Cluster %s' % str(i))
    plt.legend()
    plt.title('Inning Count vs. Cluster')
    plt.xlabel('Inning')
    plt.ylabel('Number of Occurrences')
    plt.savefig('./cluster_characterization/cluster_inning.png')
    plt.gcf().clear()

if __name__=="__main__":
    from cluster import *
    fnamecsv = './AL_pchange_vars_wins.csv'
    lbldf = cluster_into_df(fnamecsv)
    plot_clusterstats(lbldf)

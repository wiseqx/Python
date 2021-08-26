#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import re
import numpy as np
import sys
from textdistance import levenshtein
import  pyxdameraulevenshtein as dl
from fuzzywuzzy import process, fuzz
#sys.path.append('C:/Users/USER/Box/Data School choice/Data Merge')
sys.path.append('/Users/laura/Documents/ThirdYear/School Choice project/Data Merge')
from dictionarySchools import mydict
import warnings
warnings.filterwarnings("ignore")


# ## csec

# In[2]:


def read_excel(excel_file):
    return pd.read_excel(excel_file)


# In[3]:


def select_columns(df):
    
    df.columns = df.columns.str.upper()
    df.columns = ['FIRST_NAME' if 'FIRST' in x else x for x in df.columns]
    df.columns = ['LAST_NAME' if 'LAST' in x else x for x in df.columns]
    df.columns = ['DATE_OF_BIRTH' if 'DOB' in x else x for x in df.columns]
    df.columns = ['OVERALL_GRADE' if 'OVERAL' in x else x for x in df.columns]
    df.columns = ['SUBJECT' if 'SUBJ' in x else x for x in df.columns]
    df.columns = ['SCHOOL' if 'SCHOOL' in x else x for x in df.columns]
    
    df = df[['FIRST_NAME', 'LAST_NAME', 'DATE_OF_BIRTH', 'SEX', 'SCHOOL', 'SUBJECT', 'OVERALL_GRADE']]
    
    return df


# In[4]:


def handle_school(df):
    
    df["SCHOOL"] = df["SCHOOL"].str.replace("-","")
    df["SCHOOL"] = df["SCHOOL"].str.replace("'","")
    df["SCHOOL"] = df["SCHOOL"].str.replace(" ","")
    df["SCHOOL"] = df["SCHOOL"].str.replace(".","")
    df["SCHOOL"].replace(mydict, inplace=True)
    
    return df


# In[5]:


def concat_csecs(file1, file2, file3, file4, file5, file6):
    
    csec1 = read_excel(file1) if isinstance(file1, str) else file1.copy()
    csec2 = read_excel(file2) if isinstance(file2, str) else file2.copy()
    csec3 = read_excel(file3) if isinstance(file3, str) else file3.copy()
    csec4 = read_excel(file4) if isinstance(file4, str) else file4.copy()
    csec5 = read_excel(file5) if isinstance(file5, str) else file5.copy()
    csec6 = read_excel(file6) if isinstance(file6, str) else file6.copy()


    df1 = select_columns(csec1)
    df2 = select_columns(csec2)
    df3 = select_columns(csec3)
    df4 = select_columns(csec4)
    df5 = select_columns(csec5)
    df6 = select_columns(csec6)
    
    df1 = handle_school(df1)
    df2 = handle_school(df2)
    df3 = handle_school(df3)
    df4 = handle_school(df4)
    df5 = handle_school(df5)
    df6 = handle_school(df6)

    pre_name = 'PRE_' + str(''.join(filter(str.isdigit, str(file5))))
    df1.loc[:, pre_name] = 1
    df2.loc[:, pre_name] = 1
    df3.loc[:, pre_name] = 1
    df4.loc[:, pre_name] = 1
    df5.loc[:, pre_name] = 0
    df6.loc[:, pre_name] = 0
    
    concat_df = pd.concat([df1, df2, df3, df4, df5, df6], ignore_index = True)
    
    return concat_df


# In[6]:


def handle_grades(df, pre_name):
    
    df['OVERALL_GRADE'].fillna(0, inplace=True)
    
    df.OVERALL_GRADE.replace({'VI': 1, 'V': 2, 'IV': 3, 'III': 4, 'II': 5, 'I':6,
                              'ABS':0, 'UNG+':0, 'UNG*':0, 'CANC':0, 'UNG-':0, 'UNG':0, 'WIT':0,
                              'CAN':0, 'WITH':0, 'WITHHELD':0, 'CANCELLED':0, 'L':0}, inplace=True)
    
    df  = df.drop_duplicates(subset = ['FIRST_NAME','MIDDLE_NAME','LAST_NAME','DATE_OF_BIRTH',
                                       'SEX','SCHOOL','SUBJECT','OVERALL_GRADE',
                                       pre_name, 'IDENTIFIER1','IDENTIFIER2','IDENTIFIER3'], keep='first')
    
    return df
    


# In[7]:


def agg_school(df):
    
    df_schools_temp = df.drop_duplicates(subset = ['FIRST_NAME', 'MIDDLE_NAME', 'LAST_NAME',
                                          'DATE_OF_BIRTH', 'SEX','SCHOOL','IDENTIFIER1',
                                          'IDENTIFIER2','IDENTIFIER3'],keep='first')
    
    df_schools = df_schools_temp.groupby(['FIRST_NAME', 'MIDDLE_NAME', 'LAST_NAME',
                                         'DATE_OF_BIRTH', 'SEX','IDENTIFIER1','IDENTIFIER2',
                                          'IDENTIFIER3']).agg({'SCHOOL': '%'.join}).reset_index()
    
    df_schools['SCHOOL'] = df_schools['SCHOOL'].apply(lambda x :np.where('%' in x, 'multiple%' + x, x))
    
    return df_schools


# In[8]:


def agg_pre(df, pre_name):
    
    df_PRE = df.groupby(['FIRST_NAME', 'MIDDLE_NAME', 'LAST_NAME',
                        'DATE_OF_BIRTH', 'SEX', 'IDENTIFIER1','IDENTIFIER2', 
                        'IDENTIFIER3']).agg({pre_name: 'max'}).reset_index()
    
    return df_PRE


# In[9]:


def manipulate_df(df):
    
    df[['FIRST_NAME', 'MIDDLE_NAME']] = df["FIRST_NAME"].str.rsplit(expand=True, n=1) 
    df['MIDDLE_NAME'] = df['MIDDLE_NAME'].fillna('')
    df['FIRST_NAME'] = df['FIRST_NAME'].map(lambda x: re.sub(r'[^a-zA-Z]', '', x))
    df['MIDDLE_NAME'] = df['MIDDLE_NAME'].map(lambda x: re.sub(r'[^a-zA-Z]', '', str(x)))
    df['LAST_NAME'] = df['LAST_NAME'].map(lambda x: re.sub(r'[^a-zA-Z]', '', x))
    
    df['DATE_OF_BIRTH'] = pd.to_datetime(df['DATE_OF_BIRTH'], errors='coerce')
    df['DATE_OF_BIRTH'] = df["DATE_OF_BIRTH"].dt.strftime("%d%b%y")
    
    df['IDENTIFIER1'] = df['FIRST_NAME'].astype(str) + df['LAST_NAME'].astype(str) + df['DATE_OF_BIRTH'].astype(str) + df['SEX'].astype(str)
    df['IDENTIFIER2'] = df['FIRST_NAME'].astype(str) + df['MIDDLE_NAME'].astype(str) + df['LAST_NAME'].astype(str) + df['DATE_OF_BIRTH'].astype(str) + df['SEX'].astype(str)
    df['IDENTIFIER3'] = df['FIRST_NAME'].astype(str) + df['MIDDLE_NAME'].apply(lambda x: '' if len(x)==0 else x[0])+ df['LAST_NAME'].astype(str) + df['DATE_OF_BIRTH'].astype(str)+ df['SEX'].astype(str)
    
    return df


# In[10]:


def pivot_df(df):
    
    df.OVERALL_GRADE = df.OVERALL_GRADE.astype(int)
    
    new_table1 = df.pivot_table(values='OVERALL_GRADE', 
                                index=['FIRST_NAME','MIDDLE_NAME','LAST_NAME', 
                                       'SEX', 'DATE_OF_BIRTH',
                                       'IDENTIFIER1','IDENTIFIER2','IDENTIFIER3'], 
                                columns='SUBJECT').reset_index()
    
    return new_table1


# In[11]:


def csec_process(file1, file2, file3, file4, file5, file6):
    
    df = concat_csecs(file1, file2, file3, file4, file5, file6)
    pre_name = 'PRE_' + str(''.join(filter(str.isdigit, str(file5))))
    
    df = manipulate_df(df)
    df = handle_grades(df, pre_name)   
    df_schools = agg_school(df)
    df_PRE = agg_pre(df, pre_name)
    
    new_table1 = pivot_df(df)
    new_table2 = pd.merge(new_table1, df_schools, how="inner", on = ['FIRST_NAME', 'MIDDLE_NAME', 'LAST_NAME',
                                                                     'DATE_OF_BIRTH','SEX',
                                                                     'IDENTIFIER1','IDENTIFIER2','IDENTIFIER3'])
    new_table = pd.merge(new_table2, df_PRE, how="inner", on = ['FIRST_NAME', 'MIDDLE_NAME', 'LAST_NAME',
                                                                 'DATE_OF_BIRTH','SEX',
                                                                'IDENTIFIER1','IDENTIFIER2','IDENTIFIER3'])
    new_table['YEAR'] = pd.DatetimeIndex(new_table['DATE_OF_BIRTH']).year
    new_table['indexCSEC'] = new_table.index
    
    
    start_year = str(''.join(filter(str.isdigit, str(file1))))
    end_year = str(''.join(filter(str.isdigit, str(file6))))
    output_name = 'CSEC_CON_' + str(start_year) + '_' + str(end_year) + '.xlsx'
    new_table.to_excel(output_name, encoding='utf-8', index=False)
    
    return new_table


# ## csec inputs here
# Note: Years should be in ascending order

# In[12]:


# df_csec = csec_process('tb2008.xlsx', 'tb2009.xlsx', 'tb2010.xlsx', 'tb2011.xlsx', 'tb2012.xlsx', 'tb2013.xlsx')
# df_csec


# ## GSAT

# In[24]:


def manipulate_gsat(df_gsat):
    
    df_gsat['MNAME.1'] = df_gsat['MNAME.1'].fillna('')
    df_gsat['DOB_CLEAN'] = pd.to_datetime(df_gsat['DOB Converted'], errors='coerce')
    df_gsat['DOB_CLEAN'] = df_gsat["DOB_CLEAN"].dt.strftime("%d%b%y")
    df_gsat['FNAME.1'] = df_gsat['FNAME.1'].map(lambda x: re.sub(r'[^a-zA-Z]', '', str(x)))
    df_gsat['MNAME.1'] = df_gsat['MNAME.1'].map(lambda x: re.sub(r'[^a-zA-Z]', '', str(x)))
    df_gsat['SURNAME.1'] = df_gsat['SURNAME.1'].map(lambda x: re.sub(r'[^a-zA-Z]', '', str(x)))
    df_gsat['IDENTIFIER1'] = df_gsat['FNAME.1'].astype(str) + df_gsat['SURNAME.1'].astype(str) + df_gsat['DOB_CLEAN'].astype(str) + df_gsat['GENDER'].astype(str)
    df_gsat['IDENTIFIER2'] = df_gsat['FNAME.1'].astype(str) + df_gsat['MNAME.1'].astype(str) + df_gsat['SURNAME.1'].astype(str) + df_gsat['DOB_CLEAN'].astype(str) + df_gsat['GENDER'].astype(str)
    df_gsat['IDENTIFIER3'] = df_gsat['FNAME.1'].astype(str) + df_gsat['MNAME.1'].apply(lambda x: '' if len(x)==0 else x[0])+ df_gsat['SURNAME.1'].astype(str) + df_gsat['DOB_CLEAN'].astype(str)+ df_gsat['GENDER'].astype(str)
    df_gsat['PLACEDN'] = df_gsat['PLACEDN'].map(lambda x: re.sub(r'[\s.-]', '', str(x)))
    df_gsat['PLACEDN'] = df_gsat['PLACEDN'].str.replace("'","")
    df_gsat["PLACEDN"].replace(mydict, inplace=True)
    
    return df_gsat


# In[14]:


def handle_duplicates(df, ID):
    return df.drop_duplicates(subset = [ID], keep = False)


# In[15]:


def merge_step1(large_gsat_df, gsat_df, csec_df):
    
    df_inner_id2 = pd.merge(gsat_df, csec_df, on ='IDENTIFIER2', how ='inner')
    df_duplicates_s1 = large_gsat_df[~large_gsat_df.IDENTIFIER2.isin(gsat_df.IDENTIFIER2)]
    df_gsat_id2_nm_s1 = gsat_df[~gsat_df.IDENTIFIER2.isin(df_inner_id2.IDENTIFIER2)]
    
    return df_inner_id2, df_duplicates_s1, df_gsat_id2_nm_s1


# In[16]:


def merge_step2(gsat_df, csec_df):
    
    df_gsat_id2_nm_s1_nd = gsat_df.drop_duplicates(subset = ['IDENTIFIER3'], keep = False)
    df_duplicates_s2 = gsat_df[~gsat_df.IDENTIFIER3.isin(df_gsat_id2_nm_s1_nd.IDENTIFIER3)]
    df_inner_id3 = pd.merge(df_gsat_id2_nm_s1_nd, csec_df, on='IDENTIFIER3', how = 'inner')
    df_gsat_id2_nm_s2 = df_gsat_id2_nm_s1_nd[~df_gsat_id2_nm_s1_nd.IDENTIFIER3.isin(df_inner_id3.IDENTIFIER3)]
    
    return df_inner_id3, df_duplicates_s2, df_gsat_id2_nm_s2


# In[17]:


def handle_unmatched_df(df_duplicates_s1, df_duplicates_s2, df):
    
    unmatchedRound = pd.concat([df_duplicates_s1, df_duplicates_s2, df])
    unmatchedRound['SCHOOL'] = unmatchedRound['PLACEDN']
    
    return unmatchedRound


# In[18]:


def merge_step3(unmatched_df, csec_df):
    
    df_inner_id2_nm_school = pd.merge(unmatched_df, csec_df, on=['IDENTIFIER2', 'SCHOOL'], how = 'inner')
    df_gsat_id2_nm_school_nm_s3 = unmatched_df[~unmatched_df.CANDID.isin(df_inner_id2_nm_school.CANDID)]
    df_gsat_id2_nm_school_nm_s3 = df_gsat_id2_nm_school_nm_s3.drop_duplicates(subset = ['IDENTIFIER3', 'SCHOOL'], keep =False)
    
    return df_inner_id2_nm_school, df_gsat_id2_nm_school_nm_s3


# In[19]:


def merge_step4(gsat_df, csec_df):
    
    df_inner_id3_nm_school = pd.merge(gsat_df, csec_df, on=['IDENTIFIER3','SCHOOL'], how = 'inner')
    df_gsat_id3_nm_school_nm_s4 = gsat_df[~gsat_df.CANDID.isin(df_inner_id3_nm_school.CANDID)]
    df_gsat_id3_nm_school_nm_s4 = df_gsat_id3_nm_school_nm_s4.drop_duplicates(subset = ['IDENTIFIER1','SCHOOL'], keep =False)
    
    return df_inner_id3_nm_school, df_gsat_id3_nm_school_nm_s4


# In[20]:


def merge_step5(gsat_df, csec_df):
    
    df_inner_id1_nm_school = pd.merge(gsat_df, csec_df, on=['IDENTIFIER1', 'SCHOOL'], how = 'inner')
    df_gsat_id1_nm_school_nm_s5 = gsat_df[~gsat_df.CANDID.isin(df_inner_id1_nm_school.CANDID)]
    
    return df_inner_id1_nm_school, df_gsat_id1_nm_school_nm_s5


# In[32]:


def handle_matched_all(df_inner_id2, df_inner_id3, matched_s3, matched_s4, matched_s5, pre_name):
    
    matched_All = pd.concat([df_inner_id2, df_inner_id3, matched_s3, matched_s4, matched_s5], ignore_index=True)
    matched_All.drop(['IDENTIFIER1_x', 'IDENTIFIER1_y','IDENTIFIER2_x', 'IDENTIFIER2_y','IDENTIFIER3_x', 'IDENTIFIER3_y'], axis=1, inplace=True)
    
    return matched_All


# In[22]:


def match_gast_and_csec(gsat_file, df):
   
    gsat = read_excel(gsat_file) if isinstance(gsat_file, str) else gsat_file.copy()
    df_csec = read_excel(df) if isinstance(df, str) else df.copy()

    pre_name = ''.join([x for x in list(df_csec.columns) if 'PRE_' in x ])
    
    df_gsat = manipulate_gsat(gsat)
    
    df_gsat_id1 = handle_duplicates(df_gsat, 'IDENTIFIER1') 
    df_gsat_id2 = handle_duplicates(df_gsat, 'IDENTIFIER2') 
    df_gsat_id3 = handle_duplicates(df_gsat, 'IDENTIFIER3') 
    new_table_id1 = handle_duplicates(df_csec, 'IDENTIFIER1') 
    new_table_id2 = handle_duplicates(df_csec, 'IDENTIFIER2')
    new_table_id3 = handle_duplicates(df_csec, 'IDENTIFIER3')
    
    df_inner_id2, df_duplicates_s1, df_gsat_id2_nm_s1 = merge_step1(df_gsat, df_gsat_id2, new_table_id2)
    df_inner_id3, df_duplicates_s2, df_gsat_id2_nm_s2 = merge_step2(df_gsat_id2_nm_s1, new_table_id3)
    
    unmatchedRound1 = handle_unmatched_df(df_duplicates_s1, df_duplicates_s2, df_gsat_id2_nm_s2)
    
    new_table_id1school = df_csec.drop_duplicates(subset = ['IDENTIFIER1', 'SCHOOL'], keep =False)
    new_table_id1school = new_table_id1school[~new_table_id1school['SCHOOL'].str.contains('multiple')]
    
    new_table_id2school = df_csec.drop_duplicates(subset = ['IDENTIFIER2', 'SCHOOL'], keep =False)
    new_table_id2school = new_table_id2school[~new_table_id2school['SCHOOL'].str.contains('multiple')]
    
    new_table_id3school = df_csec.drop_duplicates(subset = ['IDENTIFIER3', 'SCHOOL'], keep =False)
    new_table_id3school =  new_table_id3school[~new_table_id3school['SCHOOL'].str.contains('multiple')]
    
    matched_s3, df_gsat_id2_nm_school_nm_s3 = merge_step3(unmatchedRound1, new_table_id2school)
    matched_s4, df_gsat_id3_nm_school_nm_s4 = merge_step4(df_gsat_id2_nm_school_nm_s3, new_table_id3school)
    matched_s5, df_gsat_id1_nm_school_nm_s5 = merge_step5(df_gsat_id3_nm_school_nm_s4, new_table_id1school)
    
    matched_All = handle_matched_all(df_inner_id2, df_inner_id3, matched_s3, matched_s4, matched_s5, pre_name)
    
    output_name = 'matched_All_' + str(gsat_file)
    matched_All.to_excel(output_name, encoding='utf-8',index=False)
    
    
    return matched_All
    


# ## gsat input here

# In[33]:


# matched_df = match_gast_and_csec("GSAT_2007.xlsx", df_csec)
# matched_df




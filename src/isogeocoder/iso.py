
import warnings
warnings.filterwarnings('ignore')
import re
import pandas as pd
import numpy as np
import os
import shutil
import glob 
"""
   A python  package that generates a standardized unique identity  based on a country's administrative division or any level for your use case
Use cases:
       Create unique school identity in education management information system.
       create unique health facility identity in health management information system.
       Standardize administrative level geocode.
       Area indentity generation in digital addressing system,

"""
def subregions(continent = None,level=None,sep=None):
    countries_df = pd.read_csv('countries_iso.csv')
    countries = countries_df.drop_duplicates(subset=['Alpha-3 code'])
    
    if continent == None:
        df = countries
    else:
        continent = continent.capitalize()
        df = countries[countries['Continet'].str.capitalize()==continent]
    df = df.drop_duplicates(subset=['Subregions'])
    zfill = len(str(df['M49code_Subregions'].max()))
    zfill_c = len(str(df['M49code_continent'].max()))
    if level != None and sep == None:
        df['Subregions_code'] = df['M49code_continent'].astype(str).str.zfill(zfill)+'-'+df['M49code_Subregions'].astype(str).str.zfill(zfill)
    elif sep != None:
         df['Subregions_code'] = df['M49code_continent'].astype(str).str.zfill(zfill)+sep+df['M49code_Subregions'].astype(str).str.zfill(zfill)
    else:
        df['Subregions_code'] = df['M49code_Subregions'].astype(str).str.zfill(zfill)
    df['Continent_code'] = df['M49code_continent'].astype(str).str.zfill(zfill)
    df = df[['Continet','M49code_continent','Continent_code','Subregions','M49code_Subregions','Subregions_code']]
    return df

def continents():
    countries_df = pd.read_csv('countries_iso.csv')
    countries = countries_df.drop_duplicates(subset=['Alpha-3 code'])
    df = countries.drop_duplicates(subset=['Continet'])
    df = df[['Continet','M49code_continent']]
    zfill = len(str(df['M49code_continent'].max()))
    df['Continet_code'] = df['M49code_continent'].astype(str).str.zfill(zfill)
    return df

def countries(continent=None,level=None,sep=None):
    countries_df = pd.read_csv('countries_iso.csv')
    countries = countries_df.drop_duplicates(subset=['Alpha-3 code'])
    
    if continent == None:
        df = countries
    else:
        continent = continent.capitalize()
        df = countries[countries['Continet'].str.capitalize()==continent]
    df = df.drop_duplicates(subset=['Country'])
    zfill = len(str(df['M49code_Subregions'].max()))
    zfillc = len(str(df['M49code_continent'].max()))
    zfill_country = len(str(df['M49Code_country'].max()))
    if (level != None or level !=1) and sep == None:
        df['Continent_code'] = df['M49code_continent'].astype(str).str.zfill(zfillc)
        df['Subregions_code'] = df['M49code_continent'].astype(str).str.zfill(zfillc)+'-'+df['M49code_Subregions'].astype(str).str.zfill(zfill)
        df['country_code'] = df['M49code_Subregions'].astype(str).str.zfill(zfill)+'-'+df['M49Code_country'].astype(str).str.zfill(zfill)
    if level == 1 and sep == None:
        df['Continent_code'] = df['M49code_continent'].astype(str).str.zfill(zfillc)
        df['Subregions_code'] = df['M49code_continent'].astype(str).str.zfill(zfillc)+'-'+df['M49code_Subregions'].astype(str).str.zfill(zfill)
        df['country_code'] = df['Subregions_code'].astype(str).str.zfill(zfill)+'-'+df['M49Code_country'].astype(str).str.zfill(zfill)
    elif level == 2 and sep == None:
        df['Continent_code'] = df['M49code_continent'].astype(str).str.zfill(zfillc)
        df['Subregions_code'] = df['M49code_continent'].astype(str).str.zfill(zfillc)+'-'+df['M49code_Subregions'].astype(str).str.zfill(zfill)
        df['country_code'] = df['M49code_Subregions'].astype(str).str.zfill(zfill)+'-'+df['M49Code_country'].astype(str).str.zfill(zfill)
  
    elif sep != None:
        df['Continent_code'] = df['M49code_continent'].astype(str).str.zfill(zfillc)
        df['Subregions_code'] = df['M49code_continent'].astype(str).str.zfill(zfillc)+sep+df['M49code_Subregions'].astype(str).str.zfill(zfill)
        df['country_code'] = df['M49code_Subregions'].astype(str).str.zfill(zfill)+sep+df['M49Code_country'].astype(str).str.zfill(zfill)   
    else:
        df['Subregions_code'] = df['M49code_Subregions'].astype(str).str.zfill(zfill)
        df['country_code'] = df['M49Code_country'].astype(str).str.zfill(zfill_country)    
        df['Continent_code'] = df['M49code_continent'].astype(str).str.zfill(zfillc)
    
    df = df[['Continet','M49code_continent','Continent_code','Subregions','M49code_Subregions','Subregions_code','Country','Alpha-3 code','M49Code_country','country_code']]
    return df

def country(country =None):
    countries_df = pd.read_csv('countries_iso.csv')
    countries = pd.read_csv('countries.csv')
    countries_sub = pd.read_csv('countryiso.csv')
    iso = pd.read_csv('sub_div_countries.csv')
    iso_df.loc['subdiv-code'] = iso_df['3166-2 code'].str.replace('*', '')
    iso_df[['Alpha-2 code','sub-code']] = iso_df['3166-2 code'].str.replace('*', '').str.split('-', expand = True)
    country_df = pd.merge(countries_sub,iso_df,on='Alpha-2 code',how='inner')
    countrydf = pd.merge(countries,country_df,on='Alpha-3 code',how='inner')
    zfill_country = len(str(countries_df['M49Code_country'].max()))
    zfill = len(str(countrydf['M49code_Subregions'].max()))
    zfillc = len(str(countrydf['M49code_continent'].max()))
    countrydf['Subregions_code'] = countrydf['M49code_Subregions'].astype(str).str.zfill(zfill)
    countrydf['country_code'] = countrydf['M49Code_country'].astype(str).str.zfill(zfill_country)    
    countrydf['Continent_code'] = countrydf['M49code_continent'].astype(str).str.zfill(zfillc)
    countrydf = countrydf[['Continet','M49code_continent','Continent_code','Subregions','M49code_Subregions','Subregions_code','Country','M49Code_country','country_code','Alpha-3 code','Alpha-2 code','Subdivision category',
           'Subdivision name', '3166-2 code', 'sub-code']]

    if country == None:
            df = countrydf
    else:
            country = country.capitalize()
            df = countrydf[(countrydf['Country'].str.capitalize()==country) | (countrydf['Alpha-2 code'].str.upper()==country.upper()) | (countrydf['Subregions'].str.capitalize()==country.capitalize()) | (countrydf['Continet'].str.capitalize()==country.capitalize())]
    df = df.drop_duplicates(subset=['3166-2 code'])
    return df
        
def gencode(level_df,uniqueid_df,cat_df=None,level_column=None,uniqueid_column=None,columns=None,title=None,sep=None):
        column = columns
        
        df = pd.merge(level_df,uniqueid_df,on=column,how='inner')
        if cat_df is not None:
            cat_df_col_ = cat_df.columns[0]
            df_final = pd.merge(df,cat_df,on=cat_df_col_,how='inner')
        else:
            df_final = df
        
        if sep is not None:
            df_final[title] = df_final[level_column].astype(str)+sep+df_final[uniqueid_column].astype(str)
        else:
            cat_df_col = cat_df_col_
            df_final[title] = df_final[level_column].astype(str)+df_final[uniqueid_column].astype(str)
        return df_final
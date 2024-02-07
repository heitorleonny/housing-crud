import streamlit as st
import pandas as pd
import pymysql
import sqlalchemy as engine
from database_setup.create_database import create_tables




st.write("Hello World!")

create_tables()
st.write("Criação bem sucedida")


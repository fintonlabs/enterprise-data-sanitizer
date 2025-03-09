import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from typing import Union
import json
import csv
import xml.etree.ElementTree as ET


class DataProcessor:
    """
    A class used to represent the Data Processor

    ...

    Attributes
    ----------
    data : pd.DataFrame
        a pandas dataframe to hold the data

    Methods
    -------
    load_data(file_path: str, file_type: str):
        Loads data from a file into the data attribute
    clean_data():
        Cleans the data in the data attribute
    normalize_data():
        Normalizes the data in the data attribute
    identify_inconsistencies():
        Identifies inconsistencies in the data using machine learning
    export_data(file_path: str, file_type: str):
        Exports the data in the data attribute to a file
    """

    def __init__(self):
        self.data = pd.DataFrame()

    def load_data(self, file_path: str, file_type: str) -> None:
        """
        Loads data from a file into the data attribute.

        Parameters:
        file_path (str): The path to the file
        file_type (str): The type of the file (csv, json, xml)

        Returns:
        None
        """
        if file_type == 'csv':
            self.data = pd.read_csv(file_path)
        elif file_type == 'json':
            self.data = pd.read_json(file_path)
        elif file_type == 'xml':
            tree = ET.parse(file_path)
            root = tree.getroot()
            self.data = pd.DataFrame([child.attrib for child in root])
        else:
            raise ValueError("Invalid file type. Expected 'csv', 'json', or 'xml'.")

    def clean_data(self) -> None:
        """
        Cleans the data in the data attribute.

        Returns:
        None
        """
        # Fill missing values
        imputer = SimpleImputer(strategy='mean')
        self.data = pd.DataFrame(imputer.fit_transform(self.data), columns=self.data.columns)

        # Remove duplicates
        self.data.drop_duplicates(inplace=True)

    def normalize_data(self) -> None:
        """
        Normalizes the data in the data attribute.

        Returns:
        None
        """
        # Convert categorical data to numerical data
        label_encoder = LabelEncoder()
        for column in self.data.columns:
            if self.data[column].dtype == 'object':
                self.data[column] = label_encoder.fit_transform(self.data[column])

        # Scale numerical data
        scaler = StandardScaler()
        self.data = pd.DataFrame(scaler.fit_transform(self.data), columns=self.data.columns)

    def identify_inconsistencies(self) -> None:
        """
        Identifies inconsistencies in the data using machine learning.

        Returns:
        None
        """
        # Use KMeans for anomaly detection
        kmeans = KMeans(n_clusters=2, random_state=0).fit(self.data)
        self.data['anomaly'] = kmeans.labels_

    def export_data(self, file_path: str, file_type: str) -> None:
        """
        Exports the data in the data attribute to a file.

        Parameters:
        file_path (str): The path to the file
        file_type (str): The type of the file (csv, json, xml)

        Returns:
        None
        """
        if file_type == 'csv':
            self.data.to_csv(file_path, index=False)
        elif file_type == 'json':
            self.data.to_json(file_path, orient='records')
        elif file_type == 'xml':
            root = ET.Element("root")
            for _, row in self.data.iterrows():
                child = ET.SubElement(root, "child")
                for key, value in row.items():
                    child.set(key, str(value))
            tree = ET.ElementTree(root)
            tree.write(file_path)
        else:
            raise ValueError("Invalid file type. Expected 'csv', 'json', or 'xml'.")
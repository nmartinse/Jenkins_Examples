#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building app Nerea'
            }
        }
        
        stage('Developing') {
            steps {
                echo 'Developing app Nerea'
            }
        }
        
        stage('Sleeping') {
            steps {
                sleep 30
                echo 'Sleeping'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Testing app Nerea'
            }
        }
    }
}


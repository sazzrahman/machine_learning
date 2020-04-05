FROM continuumio/anaconda3

RUN conda install -c conda-forge jupyterlab
COPY vision /opt/vision





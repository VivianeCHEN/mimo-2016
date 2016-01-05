FROM jupyter/minimal-notebook

MAINTAINER Julien Roussel <julien.roussel@gmail.com>

USER jovyan

# Install packages
RUN conda install --yes \
    CherryPy \
    beautifulsoup4 \
    Jinja2 \
    SQLAlchemy \
    lxml \
    && conda clean -yt

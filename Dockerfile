FROM public.ecr.aws/lambda/python:3.8

COPY app.py ${LAMBDA_TASK_ROOT}

COPY requirements.txt .
RUN pip3 install -r requirements.txt -t "${LAMBDA_TASK_ROOT}"

COPY init.py /tmp
COPY requirements_init.txt /tmp
RUN pip3 install -r /tmp/requirements_init.txt -t /tmp
RUN python3 /tmp/init.py

CMD [ "app.handler" ]
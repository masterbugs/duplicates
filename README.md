# Duplicate file finder in a given directory

The program aims at finding duplicate files in a given input directory. It works on Python 3.x.

### Usage
```python
python main.py sample_dir
```

### Building a docker image
```bash
sudo docker build --no-cache -t aqua-duplicates:latest .
```

### Running the container
```bash
sudo docker run -it aqua-duplicates:latest /opt/aqua/sample_dir
```

**Note:**
- /opt/aqua/sample_dir is a path which exists in the container for a quick test.
- A docker image is created and pushed to docker hub and is publicly available. The image can be pulled from anywhere.
- Name of the image: ramakrishnagudivada/aqua-duplicates:latest

### Running the container as a Kubernetes job
A yml file named duplicates.yml is provided to run the container as a Kubernetes job. The yml file is tested on kubernetes cluster version 1.17.3 and is expected to work on earlier versions as well. To change the directory for which duplicate files needs to be found, edit the duplicates.yml file args line.
```bash
sudo kubectl apply -f duplicates.yml
```

### Describe the kubernetes job
```bash
sudo kubectl describe job duplicates
```

### View the output of the job from pod logs
```bash
sudo kubectl get pods | grep duplicates
sudo kubectl logs <duplicates-vqhfm>
```

### Delete the kubernetes job
```bash
sudo kubectl delete job duplicates
```

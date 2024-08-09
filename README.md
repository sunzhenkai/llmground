# Desc
llm playground.

# Dependencies
## Library
```shell
pip install langchain langchain-community langchain-core langchain-cli langchain-ollama
pip install "langserve[all]"
```

## Ollama Server
```
127.0.0.1:11434
```
# Adding packages

```bash
# adding packages from
# https://github.com/langchain-ai/langchain/tree/master/templates
langchain app add $PROJECT_NAME

# adding custom GitHub repo packages
langchain app add --repo $OWNER/$REPO
# or with whole git string (supports other git providers):
# langchain app add git+https://github.com/hwchase17/chain-of-verification

# with a custom api mount point (defaults to `/{package_name}`)
langchain app add $PROJECT_NAME --api_path=/my/custom/path/rag
```

Note: you remove packages by their api path

```bash
langchain app remove my/custom/path/rag
```

# Setup LangSmith (Optional)
LangSmith will help us trace, monitor and debug LangChain applications.
You can sign up for LangSmith [here](https://smith.langchain.com/).
If you don't have access, you can skip this section


```shell
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_API_KEY=<your-api-key>
export LANGCHAIN_PROJECT=<your-project>  # if not specified, defaults to "default"
```

# Launch LangServe

```bash
langchain serve
```

# Running in Docker
## Building the Image
```shell
docker build . -f docker/Dockerfile -t llmground
```
## Running the Image Locally
```shell
docker run --rm -p 9015:9015 -e SENIVERSE_API_SECRET_KEY=${SENIVERSE_API_SECRET_KEY} llmground 
```
- SENIVERSE_API_SECRET_KEY: 心知天气 API 密钥
# Audio

Types:

```python
from prediction_guard.types import AudioTranscribeResponse
```

Methods:

- <code title="post /audio/transcriptions">client.audio.<a href="./src/prediction_guard/resources/audio.py">transcribe</a>(\*\*<a href="src/prediction_guard/types/audio_transcribe_params.py">params</a>) -> <a href="./src/prediction_guard/types/audio_transcribe_response.py">AudioTranscribeResponse</a></code>

# Chat

Types:

```python
from prediction_guard.types import ChatGenerateCompletionResponse
```

Methods:

- <code title="post /chat/completions">client.chat.<a href="./src/prediction_guard/resources/chat.py">generate_completion</a>(\*\*<a href="src/prediction_guard/types/chat_generate_completion_params.py">params</a>) -> <a href="./src/prediction_guard/types/chat_generate_completion_response.py">ChatGenerateCompletionResponse</a></code>

# Completions

Types:

```python
from prediction_guard.types import CompletionCreateResponse
```

Methods:

- <code title="post /completions">client.completions.<a href="./src/prediction_guard/resources/completions.py">create</a>(\*\*<a href="src/prediction_guard/types/completion_create_params.py">params</a>) -> <a href="./src/prediction_guard/types/completion_create_response.py">CompletionCreateResponse</a></code>

# Documents

Types:

```python
from prediction_guard.types import DocumentExtractTextResponse
```

Methods:

- <code title="post /documents/extract">client.documents.<a href="./src/prediction_guard/resources/documents.py">extract_text</a>(\*\*<a href="src/prediction_guard/types/document_extract_text_params.py">params</a>) -> <a href="./src/prediction_guard/types/document_extract_text_response.py">DocumentExtractTextResponse</a></code>

# Embeddings

Types:

```python
from prediction_guard.types import EmbeddingCreateResponse
```

Methods:

- <code title="post /embeddings">client.embeddings.<a href="./src/prediction_guard/resources/embeddings.py">create</a>(\*\*<a href="src/prediction_guard/types/embedding_create_params.py">params</a>) -> <a href="./src/prediction_guard/types/embedding_create_response.py">EmbeddingCreateResponse</a></code>

# McpServers

Types:

```python
from prediction_guard.types import McpServerListResponse
```

Methods:

- <code title="get /mcp_servers">client.mcp_servers.<a href="./src/prediction_guard/resources/mcp_servers.py">list</a>() -> <a href="./src/prediction_guard/types/mcp_server_list_response.py">McpServerListResponse</a></code>

# McpTools

Types:

```python
from prediction_guard.types import McpToolListResponse
```

Methods:

- <code title="get /mcp_tools">client.mcp_tools.<a href="./src/prediction_guard/resources/mcp_tools.py">list</a>() -> <a href="./src/prediction_guard/types/mcp_tool_list_response.py">McpToolListResponse</a></code>

# Models

Types:

```python
from prediction_guard.types import ModelRetrieveResponse
```

Methods:

- <code title="get /models/{capability}">client.models.<a href="./src/prediction_guard/resources/models.py">retrieve</a>(capability) -> <a href="./src/prediction_guard/types/model_retrieve_response.py">ModelRetrieveResponse</a></code>

# Rerank

Types:

```python
from prediction_guard.types import RerankCreateResponse
```

Methods:

- <code title="post /rerank">client.rerank.<a href="./src/prediction_guard/resources/rerank.py">create</a>(\*\*<a href="src/prediction_guard/types/rerank_create_params.py">params</a>) -> <a href="./src/prediction_guard/types/rerank_create_response.py">RerankCreateResponse</a></code>

# Responses

Types:

```python
from prediction_guard.types import ResponseCreateResponse
```

Methods:

- <code title="post /responses">client.responses.<a href="./src/prediction_guard/resources/responses.py">create</a>(\*\*<a href="src/prediction_guard/types/response_create_params.py">params</a>) -> <a href="./src/prediction_guard/types/response_create_response.py">ResponseCreateResponse</a></code>

# Factuality

Types:

```python
from prediction_guard.types import FactualityCheckResponse
```

Methods:

- <code title="post /factuality">client.factuality.<a href="./src/prediction_guard/resources/factuality.py">check</a>(\*\*<a href="src/prediction_guard/types/factuality_check_params.py">params</a>) -> <a href="./src/prediction_guard/types/factuality_check_response.py">FactualityCheckResponse</a></code>

# Injection

Types:

```python
from prediction_guard.types import InjectionCreateResponse
```

Methods:

- <code title="post /injection">client.injection.<a href="./src/prediction_guard/resources/injection.py">create</a>(\*\*<a href="src/prediction_guard/types/injection_create_params.py">params</a>) -> <a href="./src/prediction_guard/types/injection_create_response.py">InjectionCreateResponse</a></code>

# Pii

Types:

```python
from prediction_guard.types import PiiReplaceResponse
```

Methods:

- <code title="post /PII">client.pii.<a href="./src/prediction_guard/resources/pii.py">replace</a>(\*\*<a href="src/prediction_guard/types/pii_replace_params.py">params</a>) -> <a href="./src/prediction_guard/types/pii_replace_response.py">PiiReplaceResponse</a></code>

# Toxicity

Types:

```python
from prediction_guard.types import ToxicityCheckResponse
```

Methods:

- <code title="post /toxicity">client.toxicity.<a href="./src/prediction_guard/resources/toxicity.py">check</a>(\*\*<a href="src/prediction_guard/types/toxicity_check_params.py">params</a>) -> <a href="./src/prediction_guard/types/toxicity_check_response.py">ToxicityCheckResponse</a></code>

# Tokenize

Types:

```python
from prediction_guard.types import TokenizeGenerateResponse
```

Methods:

- <code title="post /tokenize">client.tokenize.<a href="./src/prediction_guard/resources/tokenize.py">generate</a>(\*\*<a href="src/prediction_guard/types/tokenize_generate_params.py">params</a>) -> <a href="./src/prediction_guard/types/tokenize_generate_response.py">TokenizeGenerateResponse</a></code>

# Detokenize

Types:

```python
from prediction_guard.types import DetokenizeCreateResponse
```

Methods:

- <code title="post /detokenize">client.detokenize.<a href="./src/prediction_guard/resources/detokenize.py">create</a>(\*\*<a href="src/prediction_guard/types/detokenize_create_params.py">params</a>) -> <a href="./src/prediction_guard/types/detokenize_create_response.py">DetokenizeCreateResponse</a></code>

# BGP AI Assistant

A Streamlit-based web application that provides BGP network insights using Azure OpenAI and BGPView API. The assistant helps network engineers and operators quickly analyze BGP-related information through natural language queries.

## Features

- ASN details lookup
- Prefix information retrieval
- Peer relationship analysis
- Upstream/downstream visualization
- IP address details
- Organization search
- Natural language query interface
- Integration with BGPView API
- Azure OpenAI-powered insights

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-repo/gpt4o-mini-BGP-Assistant.git
cd gpt4o-mini-BGP-Assistant
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

### Azure AI Foundry Setup

1. **Create Azure OpenAI Resource**
   - Navigate to Azure Portal
   - Create a new OpenAI resource
   - Select the appropriate region and pricing tier

2. **Set Up Assistant**
   - In Azure AI Studio, create a new Assistant
   - Configure the Assistant with the provided tool schemas
   - Enable function calling capabilities

3. **Configure Vector Store**
   - Create a new Vector Store in Azure AI Studio
   - Configure the vector embeddings model
   - Set up the appropriate indexing strategy

4. **Obtain API Keys**
   - In Azure Portal, navigate to your OpenAI resource
   - Under "Keys and Endpoint", copy:
     - Endpoint URL
     - API Key
     - Assistant ID
     - Vector Store ID

### Environment Variables

Create a `.env` file with the following variables:

```bash
BGPVIEW_BASE_URL=https://api.bgpview.io/
AZURE_OPENAI_ENDPOINT=your-endpoint
AZURE_OPENAI_API_KEY=your-api-key
AZURE_OPENAI_ASSISTANT_ID=your-assistant-id
AZURE_VECTORSTORE_ID=your-vectorstore-id
```

### VectorDB Configuration

The VectorDB is used for storing and retrieving BGP-related knowledge. Configure it through the Azure AI Studio interface with:

- Appropriate chunking strategy
- Relevant metadata fields
- Proper indexing parameters

## Usage

1. Start the Streamlit app:
```bash
streamlit run Azure_gpt4o-mini_BGP_Assistant.py
```

2. Example queries:
- "Show details for ASN 12345"
- "What prefixes are announced by ASN 67890?"
- "Who are the peers of ASN 54321?"
- "Show upstream providers for ASN 98765"

## Tool Schemas

### get_bgp_asn_details
```json
{
  "name": "get_bgp_asn_details",
  "description": "Retrieve details about a specific BGP ASN.",
  "parameters": {
    "type": "object",
    "properties": {
      "asn": {
        "type": "string",
        "description": "The Autonomous System Number to get details for."
      }
    },
    "required": [
      "asn"
    ]
  }
}
```

[Other tool schemas would be documented similarly...]

## Dependencies

- Python 3.8+
- Streamlit
- Azure OpenAI
- BGPView API
- Python-dotenv

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

# 🎧 blendify

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
[![Spotify](https://img.shields.io/badge/Spotify-1ED760?logo=spotify&logoColor=white)](#)
[![ChatGPT](https://img.shields.io/badge/ChatGPT-74aa9c?logo=openai&logoColor=white)](#)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](#LICENSE)

> Generate smart, genre-blending Spotify playlists powered by OpenAI and Python.

**blendify** lets you create Spotify playlists that feel like collaborative, AI-curated musical journeys — inspired by Hathor’s fusion radio feature.

---

## 🚀 Features

- 🎶 Generate playlists that fuse multiple genres or artists.
- 🤖 Uses OpenAI to enhance playlist curation.
- 🎛️ Simple configuration for full control.
- 💡 Lightweight and easy to set up.

---

## 🛠️ Installation

### 1. Prerequisites

Install [uv](https://docs.astral.sh/uv/#installation):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Clone the Repo

```bash
git clone https://github.com/dsabecky/blendify.git
cd blendify
```

### 3. Create Your Spotify Application

Create one here: [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/create)

### 4. Obtain your OpenAI API Key

Obtain it here: [OpenAI API Portal](https://platform.openai.com/api-keys)

---

## ⚙️ Configuration

1. Rename the config template:
```bash
mv config.py.example config.py
```

2. Edit `config.py` with your credentials:

```python
# Spotify API
SPOTIFY_CLIENT_ID = ''       # Your Spotify Client ID
SPOTIFY_CLIENT_SECRET = ''   # Your Spotify Secret
SPOTIFY_REDIRECT_URI = 'http://127.0.0.1:8080'

# OpenAI API
OPENAI_API_KEY = ''          # Your OpenAI API key
OPENAI_MODEL = 'gpt-4.1'     # Supports non-reasoning models only
OPENAI_TEMPERATURE = 1

# Playlist Configuration
PLAYLIST_ID = ''             # Target playlist ID
PLAYLIST_LENGTH = 100        # Between 10 and 100
```

---

## ▶️ Running the App

Use `uv` to run `blendify`:

```bash
uv run blendify.py
```
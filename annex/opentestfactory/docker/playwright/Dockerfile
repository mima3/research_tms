# Node.js 用 Playwright（ブラウザ内蔵）。Playwright 自体はプロジェクト側で npm i する想定
FROM mcr.microsoft.com/playwright:v1.53.0-noble

# opentf-agent は Python 製なので python/pip を追加してインストール
RUN apt-get update \
 && apt-get install -y --no-install-recommends git python3 python3-pip \
 && rm -rf /var/lib/apt/lists/* \
 && pip3 install --no-cache-dir --break-system-packages opentf-agent

WORKDIR /workspace

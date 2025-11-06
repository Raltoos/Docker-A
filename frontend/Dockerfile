# frontend/Dockerfile
FROM node:18-alpine

WORKDIR /usr/src/app

# Copy only package files first for better caching
COPY package.json package-lock.json* ./

# Use npm ci if package-lock exists, otherwise npm install
RUN if [ -f package-lock.json ]; then npm ci --omit=dev; else npm install --omit=dev; fi

COPY . .

ENV PORT=3000
# default backend url; overridden in docker-compose for runtime
ENV BACKEND_URL=http://backend:5000

EXPOSE 3000
CMD ["node", "app.js"]

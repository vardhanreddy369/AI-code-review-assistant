FROM node:18-alpine

WORKDIR /app

# Copy package files
COPY package.json ./

# Install dependencies  
RUN npm install 2>&1 && npm install -g vite

# Copy application code
COPY . .

# Expose port
EXPOSE 3000

# Start development server
CMD ["npm", "run", "dev"]



# Use the official Node.js 16 image as a parent image
FROM node:17

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json (if available) to the working directory
COPY package*.json ./

# Install dependencies
# RUN npm install

# Copy the rest of your application's source code from your host to your image filesystem
COPY . .

# Your application will listen on port 8002 by default, make sure this matches with your application's port
EXPOSE 3000

# Define the command to run your application
CMD ["node", "index.js"]
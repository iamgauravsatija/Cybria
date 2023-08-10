# Use a Node.js base image
FROM node:18.16.0 AS builder

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Copy the rest of the application code to the container
COPY . .


# Install dependencies
RUN npm i && npm run ng build

EXPOSE 4200



# Build the Angular app
# RUN npm run build

# RUN ng serve

# Use the official NGINX image as the final image
FROM nginx

WORKDIR /usr/share/nginx/html 

RUN rm -rf ./*

COPY cybria.conf /etc/nginx/nginx.conf

# Copy the built Angular app to the NGINX web server's public folder
COPY --from=builder /app/dist/cybria .

RUN chmod 0444 /etc/nginx/nginx.conf

# RUN nginx -g daemon off;
# RUN ng server --open

# Expose the port that NGINX listens on (default: 80)
EXPOSE 80

# Start the NGINX server
CMD ["nginx", "-g", "daemon off;"]


FROM node:lts-slim AS final
WORKDIR /frontend
COPY .output ./.output
ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=3000
EXPOSE 3000
ENTRYPOINT ["node", "./.output/server/index.mjs"]

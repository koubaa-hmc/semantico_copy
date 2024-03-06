# Information Portal

In this repository the front-end of the Information Portal is developed.

## Repository structure

- `release` branch contains the stable production code. The latest Docker images of this code can be found here: registry.hzdr.de/hmc/hmc/cct-1-mapping/information-portal/frontend/frontend:latest
- `main` branch is the staging branch, this branch also contains stable production ready code, but if a bug is found the hot fixes for them are tested here before they are pushed into the `release` branch. Docker images are available here: registry.hzdr.de/hmc/hmc/cct-1-mapping/information-portal/frontend/frontend-staging:latest
- `dev` branch is where the development happens. This code is updated regularly with new features and fixes. After a sprint has ended and the code is stable it is pushed into the `staging` branch. Docker images of the current development can be found here: registry.hzdr.de/hmc/hmc/cct-1-mapping/information-portal/frontend/frontend-dev:latest
- every other branches are feature branches used to develop unique features/fixes to make IP frontend more awesome!

## Development

Look at the [Nuxt 3 documentation](https://nuxt.com/docs/getting-started/introduction) to learn more.

## Setup

Make sure to install the dependencies:

```bash
# yarn
yarn install

# npm
npm install
```
## Development Server

Start the development server on http://localhost:3000

```bash
# yarn
yarn dev 

# npm
npm run dev
```

## Production

Build the application for production:

```bash
# yarn
yarn build

# npm
npm run build

```

Locally preview production build:

```bash
# yarn
yarn preview

# npm
npm run preview
```

Check out the [deployment documentation](https://nuxt.com/docs/getting-started/deployment) for more information.

## End-to-End-Testing
Tests are done using [Playwright](https://playwright.dev/).
Dependencies need to be installed via  
```bash
npx playwright install --with-deps
```
Run tests on CLI 
```bash
# yarn
yarn playwright-cli

# npm
npm run playwright-cli
```

Run tests using Playwright GUI
```bash
# yarn
yarn playwright-ui

# npm
npm run playwright-ui
```

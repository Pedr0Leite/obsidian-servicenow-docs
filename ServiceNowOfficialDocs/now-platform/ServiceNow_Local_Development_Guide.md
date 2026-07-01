# ServiceNow Application Local Development Guide (SDK CLI)

Practical guide to pull an application from ServiceNow (unit4dev1), work locally, and avoid conflicts when synchronizing changes.

## 1. Authenticate

```bash
npx @servicenow/sdk auth --add https://unit4dev1.service-now.com --type basic --alias unit4dev1
```

## 2. Initial Pull of Application

```bash
npx @servicenow/sdk init --from <APPLICATION_SYS_ID> --auth unit4dev1
```

## 3. Install Dependencies

```bash
npm install
```

## 4. Sync from Instance (Transform)

```bash
now-sdk transform --auth unit4dev1
```

## 5. Build

```bash
now-sdk build
```

## 6. Deploy

```bash
now-sdk install --auth unit4dev1
```

## Understanding transform

The `transform` command synchronizes metadata changes from the instance into your local project by converting them into source code. It should be used frequently to avoid drift between local and instance versions.

## How to Avoid Conflicts with transform

- Always run `transform` before starting work.
- Avoid editing the same records both locally and directly in the instance at the same time.
- Use a consistent workflow (`pull → change → build → deploy`).
- If unsure, run `transform` again before deploying.

## Examples of Changes Made Directly on Instance

- Updating a Business Rule from the UI
- Editing a Script Include in Studio
- Changing form layout or UI Policy
- Modifying ACLs or roles

If these changes are not pulled using `transform`, local code may overwrite them during deployment.

## Recommended Daily Workflow

```bash
# sync first
now-sdk transform --auth unit4dev1

# develop locally

# build and deploy
now-sdk build
now-sdk install --auth unit4dev1
```

> Classification - Business (TLP Green)

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const templatePath = path.join(repoRoot, "CORRETTO", "Dockerfile.template");
const versions = [8, 11, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26];
const template = fs.readFileSync(templatePath, "utf8");

if (!template.includes("@@JAVA_VERSION@@")) {
  throw new Error("Corretto Dockerfile template is missing @@JAVA_VERSION@@");
}

for (const version of versions) {
  const directory = path.join(repoRoot, "CORRETTO", String(version));
  const dockerfile = template.replaceAll("@@JAVA_VERSION@@", String(version));
  fs.mkdirSync(directory, { recursive: true });
  fs.writeFileSync(path.join(directory, "Dockerfile"), dockerfile);
}

console.log(`Generated ${versions.length} Corretto Dockerfiles: ${versions.join(", ")}`);

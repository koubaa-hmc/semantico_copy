export enum MappingCategory {
  "Repositories" = "repository",
  "Terminologies" = "terminology",
  "Software" = "software",
  "Data Sources" = "data_source",
  "Data Formats" = "data_format",
  "Licenses" = "license",
  "Organizations" = "organization",
  "Policies" = "policy",
  "Documents" = "document",
  "Schema Crosswalks" = "schema_crosswalk",
  "Methods" = "method",
  "Datasets" = "dataset",
  "Links" = "link",
  "Metadata Standards" = "metadata_standard",
  "PID Systems" = "pid_system",
  "Training Materials" = "training_material",
}

export function isMappingCategoryKey(
  entry: string
): entry is keyof typeof MappingCategory {
  return entry in MappingCategory;
}

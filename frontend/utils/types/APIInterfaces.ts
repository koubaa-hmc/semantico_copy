import type { IPBaseObject } from "~/utils/types/CommonProperties";
import { HMCHub } from "~/utils/types/HMCHub";

export interface PaginationResult {
  /** The actual result data */
  data: IPBaseObject[];
  /** The cardinality of the result set */
  count: number;
  /** The total number of items in database for the given category */
  totalCount: number;
}

export interface PaginationParameter {
  limit?: number;
  offset?: number;
}

/** Used for path /MappingItem/search */
export interface SearchParameter extends PaginationParameter {
  searchText: string;
  hub?: HMCHub;
}

import { HMCHub } from "~/utils/types/HMCHub";
import { MappingCategory } from "~/utils/types/MappingCategory";
import type { IPBaseObject } from "~/utils/types/CommonProperties";
import type {
  PaginationParameter,
  PaginationResult,
  SearchParameter
} from "~/utils/types/APIInterfaces";

/**
 * Get all mapping items belonging to a given category.
 * @param category The category of the mapping items.
 * @param limit    Optional: restrict the result set to a specific number
 * @param offset   Optional: retrieving the result set starting with a given offset
 */
export const getCategory = (
  category: MappingCategory,
  limit?: number,
  offset?: number
) => {
  const {
    public: { apiBaseUrl },
  } = useRuntimeConfig();

  const params: PaginationParameter = {};

  if (limit && limit >= 0) {
    params.limit = limit;
  }
  if (offset && offset >= 0) {
    params.offset = offset;
  }

  return useFetch<PaginationResult>(`/MappingItem/categories/${category}`, {
    key: `${category}/${offset}/${limit}`,
    baseURL: apiBaseUrl,
    method: "get",
    parseResponse: JSON.parse,
    params,
  });
};

/**
 * Retrieve a specific mapping item by id.
 * @param id The id of the item.
 */
export const getItem = (id: string) => {
  const {
    public: { apiBaseUrl },
  } = useRuntimeConfig();

  return useFetch<IPBaseObject>(`/MappingItem/${id}`, {
    key: id,
    baseURL: apiBaseUrl,
    method: "get",
    parseResponse: JSON.parse,
  });
};

/**
 * Search for mapping items given a 'searchText'. The search can be restricted to a specific hub.
 * @param searchText The term to look for in the data.
 * @param hub A specific to restrict search space.
 * @param limit    Optional: restrict the result set to a specific number
 * @param offset   Optional: retrieving the result set starting with a given offset
 */
export const search = (
  searchText: string,
  hub?: HMCHub,
  limit?: number,
  offset?: number
) => {
  const {
    public: { apiBaseUrl },
  } = useRuntimeConfig();

  const params: SearchParameter = {
    searchText,
  };

  if (hub) {
    params.hub = hub;
  }
  if (limit) {
    params.limit = limit;
  }
  if (offset) {
    params.offset = offset;
  }

  return useFetch<PaginationResult>(`/MappingItem/search`, {
    params,
    baseURL: apiBaseUrl,
    method: "get",
    parseResponse: JSON.parse,
  });
};

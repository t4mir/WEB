import { Games } from './category'
export interface Company {
    id: number,
    name: string,
    products: Games[]
}
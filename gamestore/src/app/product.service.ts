import { Injectable } from '@angular/core';
import { Games } from '../app/category';
import { Observable, of } from 'rxjs';
import { AllCategories } from './games';
import { AllProd } from './categories';
import { catchError, map, tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ProductService {

  getAllProd(): Observable<Games[]> {
    return of(AllProd);
  }
  serviceWithProd = AllCategories;
  allCateg = AllProd;

  constructor(){ }
  getProductsByCategoryId(id): Observable<any> {
    const neededCategory = this.serviceWithProd.find(category => category.categoryId === id);
    return of(neededCategory.products);
  }

  private gamesUrl = 'api/games';

  // searchProduct (prodName: string): Observable<Games[]> {
  //   if(!prodName.trim()) {
  //     return of([]);
  //   }
  //   return this.http.get<Games[]>(`${this.gamesUrl}/?name=${prodName}`).pipe (
  //     tap(x => x.length ?
  //       // this.log(`found heroes matching "${prodName}"`) :
  //       // this.log(`no heroes matching "${prodName}"`)),
  //   );
  // }

  getFromAllProductsByCategoryId(categoryId): Observable<any> {
    const neededProducts = this.allCateg.filter(actions => actions.categoryID === categoryId);
    return of(neededProducts);
  }

  getCategories() : Observable<any> {
    return of(this.serviceWithProd);
  }

  getProductById(id): Observable<any> {
    const neededProduct = this.allCateg.find(product => product.id === id);
    return of(neededProduct)
  }
}

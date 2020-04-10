import { Injectable } from '@angular/core';
import {AllProd} from '../app/categories';
import { Observable, of } from 'rxjs';
import {Games} from '../app/category';

@Injectable({
  providedIn: 'root'
})
export class CategoriesService {

  serviceProd = AllProd;

  getProductList() : Observable<Games[]> {
    return of(this.serviceProd);
  }

  getProductbyId(id) : Observable<any> {
    const neededProductList = this.serviceProd.find(prodPage => prodPage.categoryID === id);
    return of (neededProductList);
  }
  constructor() { }
}

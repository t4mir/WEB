import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import {Games} from '../app/category';
import { HttpClient } from '@angular/common/http';
import { Company } from './companies';
import { Category } from './categorys';

@Injectable({
  providedIn: 'root'
})
export class CategoriesService {
  BASE_URL = 'http://localhost:8000'
  constructor(private http : HttpClient) { }

  getCategories () : Observable<Category[]> {
    return this.http.get<Category[]>(`${this.BASE_URL}/api/categories`);
  }

  getGamesbyCategory(id) : Observable<Category> {
    return this.http.get<Category>(`${this.BASE_URL}/api/categories/${id}`)
  }

}

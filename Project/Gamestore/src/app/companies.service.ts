import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Company } from './companies';
import { Observable } from 'rxjs'

@Injectable({
  providedIn: 'root'
})
export class CompaniesService {
  BASE_URL = 'http://localhost:8000'
  constructor(private http : HttpClient) { }

  getCompanies () : Observable<Company[]> {
    return this.http.get<Company[]>(`${this.BASE_URL}/api/companies`)
  }

  getGamesByCompany (id) : Observable<Company> {
    return this.http.get<Company>(`${this.BASE_URL}/api/companies/${id}`)
  }
}

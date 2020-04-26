import { Component, OnInit } from '@angular/core';
import { CompaniesService } from '../companies.service';
import { Company } from '../companies';

@Component({
  selector: 'app-companies',
  templateUrl: './companies.component.html',
  styleUrls: ['./companies.component.css']
})
export class CompaniesComponent implements OnInit {
  companies : Company[] = [];
  constructor(private compService : CompaniesService) { }

  ngOnInit(): void {
    this.getCompanies();
  }

  getCompanies () {
    this.compService.getCompanies().subscribe(com => {
      this.companies = com;
    })
  }

}

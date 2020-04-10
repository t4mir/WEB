import { Component, OnInit } from '@angular/core';
import { ProductService } from '../product.service';
@Component({
  selector: 'app-categories',
  templateUrl: './categories.component.html',
  styleUrls: ['./categories.component.css']
})

export class CategoriesComponent implements OnInit {
  categories : any = [];
  constructor(public prodServ : ProductService){}

  ngOnInit():void {
    this.getProductList();
  }

  getProductList() {
    const categoryObservable = this.prodServ.getCategories();
    categoryObservable.subscribe(product => this.prodServ = product);
  }
}

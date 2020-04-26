import { Component, OnInit } from '@angular/core';
import { ProductService } from '../product.service';
import { Category } from '../categorys';
import { CategoriesService } from '../categories.service';
@Component({
  selector: 'app-categories',
  templateUrl: './categories.component.html',
  styleUrls: ['./categories.component.css']
})

export class CategoriesComponent implements OnInit {
  categories : Category[] = [];
  constructor(public catServ : CategoriesService){}

  ngOnInit():void {
    // this.getProductList();
  }

  getCategories () {
    this.catServ.getCategories().subscribe(cats => {
      this.categories = cats
    });
  }
}

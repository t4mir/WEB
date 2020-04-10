import { Component, OnInit } from '@angular/core';
import { ProductService } from '../product.service';
import { ActivatedRoute } from '@angular/router';
import { Wish } from '../wish'; 
 
@Component({
  selector: 'app-products-list',
  templateUrl: './products-list.component.html',
  styleUrls: ['./products-list.component.css']
})
export class ProductsListComponent implements OnInit {

  productsonPage : any;

  constructor(private route: ActivatedRoute, private prodServ : ProductService) { }

  ngOnInit(): void {
    this.getProductList();
  }

  getProductList() {
    const id = +this.route.snapshot.paramMap.get('categoryId');
    const currentProductList = this.prodServ.getFromAllProductsByCategoryId(id);
    currentProductList.subscribe(product => this.productsonPage = product);
  }

  name: string;
  price: number;
  category: string;
  os:string;
   
  wishes: Wish[] = [];
  categories: string[] = ["Action","Simulator","Sport","Strategy"];
   
  addWish(){
      this.wishes.push(new Wish(this.name, this.price, this.category,this.os));
  }
   
   
}

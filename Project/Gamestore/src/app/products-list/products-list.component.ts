import { Component, OnInit } from '@angular/core';
import { ProductService } from '../product.service';
import { ActivatedRoute } from '@angular/router';
import { Wish } from '../wish'; 
import { Games } from '../category';
import { CompaniesService } from '../companies.service';
import { CategoriesService } from '../categories.service';
import { Category } from '../categorys';
 
@Component({
  selector: 'app-products-list',
  templateUrl: './products-list.component.html',
  styleUrls: ['./products-list.component.css']
})
export class ProductsListComponent implements OnInit {

  productsonPage : any;

  constructor(private catsServ : CategoriesService, private route: ActivatedRoute, private prodServ : ProductService) { }
  games : Category;
  ngOnInit(): void {
    this.getGamesten();
  }
  getGamesten() {
    const id = +this.route.snapshot.paramMap.get('id');
    this.catsServ.getGamesbyCategory(id).subscribe(gam => this.games = gam);
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
  removeWish() {
    this.wishes.pop()
  }
}

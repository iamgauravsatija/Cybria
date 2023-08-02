import { animate, query, stagger, state, style, transition, trigger } from '@angular/animations';
import { Component, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-nav-bar',
  templateUrl: './nav-bar.component.html',
  styleUrls: ['./nav-bar.component.css'],
  animations: [
    trigger('navButtonAnimation', [
      transition('* => *', [
        query('.slide-in', style({ transform: 'translateX(+400%)' })),
        query('.slide-in',
          stagger('100ms', [
            animate('1s ease-in', style({ transform: 'translateX(0)'})),
          ])
        )
      ])
    ]),
    trigger('burgerButtonAnimation', [
      state('vertical', style({ transform: 'rotate(0deg)' })),
      state('horizontal', style({ transform: 'rotate(90deg)' })),
      transition('horizontal => vertical', animate('300ms ease-in')),
      transition('vertical => horizontal', animate('300ms ease-in'))
    ])
  ]
})


export class NavBarComponent {
  
  @Output() sideNavToggled = new EventEmitter<boolean>();
  menuStatus: boolean = false;

  constructor() { }

  burgerButtonPosition = 'vertical';

  changeBurgerButtonPosition() {
    if(this.burgerButtonPosition === 'horizontal') {
      this.burgerButtonPosition = 'vertical';
    } else {
      this.burgerButtonPosition = 'horizontal';
    }
  }

  SideNavToggle() {
    this.menuStatus = !this.menuStatus;
    this.sideNavToggled.emit(this.menuStatus);
  }
}

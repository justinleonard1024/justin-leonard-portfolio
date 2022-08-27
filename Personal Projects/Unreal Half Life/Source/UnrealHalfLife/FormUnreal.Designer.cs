/********************************
 * Unreal Half Life
 * FormUnreal.Designer.cs
 * Created by Justin Leonard
********************************/

namespace UnrealHalfLife
{
    partial class FormUnreal
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(FormUnreal));
            this.model_panel = new System.Windows.Forms.Panel();
            this.model_button_high = new System.Windows.Forms.RadioButton();
            this.model_button_medium = new System.Windows.Forms.RadioButton();
            this.model_button_low = new System.Windows.Forms.RadioButton();
            this.model_label = new System.Windows.Forms.Label();
            this.texture_button_high = new System.Windows.Forms.RadioButton();
            this.texture_button_medium = new System.Windows.Forms.RadioButton();
            this.texture_button_low = new System.Windows.Forms.RadioButton();
            this.texture_label = new System.Windows.Forms.Label();
            this.texture_panel = new System.Windows.Forms.Panel();
            this.shader_panel = new System.Windows.Forms.Panel();
            this.shader_button_high = new System.Windows.Forms.RadioButton();
            this.shader_button_medium = new System.Windows.Forms.RadioButton();
            this.shader_button_low = new System.Windows.Forms.RadioButton();
            this.shader_label = new System.Windows.Forms.Label();
            this.water_label = new System.Windows.Forms.Label();
            this.water_panel = new System.Windows.Forms.Panel();
            this.water_button_high = new System.Windows.Forms.RadioButton();
            this.water_button_low = new System.Windows.Forms.RadioButton();
            this.shadow_button_low = new System.Windows.Forms.RadioButton();
            this.shadow_label = new System.Windows.Forms.Label();
            this.shadow_panel = new System.Windows.Forms.Panel();
            this.shadow_button_high = new System.Windows.Forms.RadioButton();
            this.vsync_label = new System.Windows.Forms.Label();
            this.vsync_panel = new System.Windows.Forms.Panel();
            this.vsync_button_on = new System.Windows.Forms.RadioButton();
            this.vsync_button_off = new System.Windows.Forms.RadioButton();
            this.preset_label = new System.Windows.Forms.Label();
            this.preset_combobox = new System.Windows.Forms.ComboBox();
            this.play_button = new System.Windows.Forms.Button();
            this.imageMain = new System.Windows.Forms.PictureBox();
            this.pictureBox2 = new System.Windows.Forms.PictureBox();
            this.model_panel.SuspendLayout();
            this.texture_panel.SuspendLayout();
            this.shader_panel.SuspendLayout();
            this.water_panel.SuspendLayout();
            this.shadow_panel.SuspendLayout();
            this.vsync_panel.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.imageMain)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            this.SuspendLayout();
            // 
            // model_panel
            // 
            this.model_panel.BackColor = System.Drawing.SystemColors.ControlLight;
            this.model_panel.Controls.Add(this.model_button_high);
            this.model_panel.Controls.Add(this.model_button_medium);
            this.model_panel.Controls.Add(this.model_button_low);
            this.model_panel.Controls.Add(this.model_label);
            this.model_panel.Location = new System.Drawing.Point(26, 321);
            this.model_panel.Name = "model_panel";
            this.model_panel.Size = new System.Drawing.Size(129, 146);
            this.model_panel.TabIndex = 0;
            // 
            // model_button_high
            // 
            this.model_button_high.AutoSize = true;
            this.model_button_high.Font = new System.Drawing.Font("Arial Narrow", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.model_button_high.Location = new System.Drawing.Point(36, 97);
            this.model_button_high.Name = "model_button_high";
            this.model_button_high.Size = new System.Drawing.Size(54, 24);
            this.model_button_high.TabIndex = 3;
            this.model_button_high.Text = "High";
            this.model_button_high.UseVisualStyleBackColor = true;
            this.model_button_high.CheckedChanged += new System.EventHandler(this.model_button_high_CheckedChanged);
            // 
            // model_button_medium
            // 
            this.model_button_medium.AutoSize = true;
            this.model_button_medium.Font = new System.Drawing.Font("Arial Narrow", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.model_button_medium.Location = new System.Drawing.Point(36, 67);
            this.model_button_medium.Name = "model_button_medium";
            this.model_button_medium.Size = new System.Drawing.Size(75, 24);
            this.model_button_medium.TabIndex = 2;
            this.model_button_medium.Text = "Medium";
            this.model_button_medium.UseVisualStyleBackColor = true;
            this.model_button_medium.CheckedChanged += new System.EventHandler(this.model_button_medium_CheckedChanged);
            // 
            // model_button_low
            // 
            this.model_button_low.AutoSize = true;
            this.model_button_low.Font = new System.Drawing.Font("Arial Narrow", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.model_button_low.Location = new System.Drawing.Point(36, 37);
            this.model_button_low.Name = "model_button_low";
            this.model_button_low.Size = new System.Drawing.Size(51, 24);
            this.model_button_low.TabIndex = 1;
            this.model_button_low.Text = "Low";
            this.model_button_low.UseVisualStyleBackColor = true;
            this.model_button_low.CheckedChanged += new System.EventHandler(this.model_button_low_CheckedChanged);
            // 
            // model_label
            // 
            this.model_label.AutoSize = true;
            this.model_label.BackColor = System.Drawing.SystemColors.ControlLight;
            this.model_label.Font = new System.Drawing.Font("Arial Narrow", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.model_label.Location = new System.Drawing.Point(5, 0);
            this.model_label.Name = "model_label";
            this.model_label.Size = new System.Drawing.Size(121, 25);
            this.model_label.TabIndex = 0;
            this.model_label.Text = "Model Quality";
            // 
            // texture_button_high
            // 
            this.texture_button_high.AutoSize = true;
            this.texture_button_high.Font = new System.Drawing.Font("Arial Narrow", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.texture_button_high.Location = new System.Drawing.Point(36, 97);
            this.texture_button_high.Name = "texture_button_high";
            this.texture_button_high.Size = new System.Drawing.Size(54, 24);
            this.texture_button_high.TabIndex = 3;
            this.texture_button_high.TabStop = true;
            this.texture_button_high.Text = "High";
            this.texture_button_high.UseVisualStyleBackColor = true;
            this.texture_button_high.CheckedChanged += new System.EventHandler(this.texture_button_high_CheckedChanged);
            // 
            // texture_button_medium
            // 
            this.texture_button_medium.AutoSize = true;
            this.texture_button_medium.Font = new System.Drawing.Font("Arial Narrow", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.texture_button_medium.Location = new System.Drawing.Point(36, 67);
            this.texture_button_medium.Name = "texture_button_medium";
            this.texture_button_medium.Size = new System.Drawing.Size(75, 24);
            this.texture_button_medium.TabIndex = 2;
            this.texture_button_medium.TabStop = true;
            this.texture_button_medium.Text = "Medium";
            this.texture_button_medium.UseVisualStyleBackColor = true;
            this.texture_button_medium.CheckedChanged += new System.EventHandler(this.texture_button_medium_CheckedChanged);
            // 
            // texture_button_low
            // 
            this.texture_button_low.AutoSize = true;
            this.texture_button_low.Font = new System.Drawing.Font("Arial Narrow", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.texture_button_low.Location = new System.Drawing.Point(36, 37);
            this.texture_button_low.Name = "texture_button_low";
            this.texture_button_low.Size = new System.Drawing.Size(51, 24);
            this.texture_button_low.TabIndex = 1;
            this.texture_button_low.TabStop = true;
            this.texture_button_low.Text = "Low";
            this.texture_button_low.UseVisualStyleBackColor = true;
            this.texture_button_low.CheckedChanged += new System.EventHandler(this.texture_button_low_CheckedChanged);
            // 
            // texture_label
            // 
            this.texture_label.AutoSize = true;
            this.texture_label.BackColor = System.Drawing.SystemColors.ControlLight;
            this.texture_label.Font = new System.Drawing.Font("Arial Narrow", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.texture_label.Location = new System.Drawing.Point(0, 0);
            this.texture_label.Name = "texture_label";
            this.texture_label.Size = new System.Drawing.Size(132, 25);
            this.texture_label.TabIndex = 0;
            this.texture_label.Text = "Texture Quality";
            // 
            // texture_panel
            // 
            this.texture_panel.BackColor = System.Drawing.SystemColors.ControlLight;
            this.texture_panel.Controls.Add(this.texture_button_high);
            this.texture_panel.Controls.Add(this.texture_button_medium);
            this.texture_panel.Controls.Add(this.texture_button_low);
            this.texture_panel.Controls.Add(this.texture_label);
            this.texture_panel.Location = new System.Drawing.Point(161, 321);
            this.texture_panel.Name = "texture_panel";
            this.texture_panel.Size = new System.Drawing.Size(129, 146);
            this.texture_panel.TabIndex = 4;
            // 
            // shader_panel
            // 
            this.shader_panel.BackColor = System.Drawing.SystemColors.ControlLight;
            this.shader_panel.Controls.Add(this.shader_button_high);
            this.shader_panel.Controls.Add(this.shader_button_medium);
            this.shader_panel.Controls.Add(this.shader_button_low);
            this.shader_panel.Controls.Add(this.shader_label);
            this.shader_panel.Location = new System.Drawing.Point(296, 321);
            this.shader_panel.Name = "shader_panel";
            this.shader_panel.Size = new System.Drawing.Size(129, 146);
            this.shader_panel.TabIndex = 5;
            // 
            // shader_button_high
            // 
            this.shader_button_high.AutoSize = true;
            this.shader_button_high.Font = new System.Drawing.Font("Arial Narrow", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.shader_button_high.Location = new System.Drawing.Point(36, 97);
            this.shader_button_high.Name = "shader_button_high";
            this.shader_button_high.Size = new System.Drawing.Size(54, 24);
            this.shader_button_high.TabIndex = 3;
            this.shader_button_high.TabStop = true;
            this.shader_button_high.Text = "High";
            this.shader_button_high.UseVisualStyleBackColor = true;
            this.shader_button_high.CheckedChanged += new System.EventHandler(this.shader_button_high_CheckedChanged);
            // 
            // shader_button_medium
            // 
            this.shader_button_medium.AutoSize = true;
            this.shader_button_medium.Font = new System.Drawing.Font("Arial Narrow", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.shader_button_medium.Location = new System.Drawing.Point(36, 67);
            this.shader_button_medium.Name = "shader_button_medium";
            this.shader_button_medium.Size = new System.Drawing.Size(75, 24);
            this.shader_button_medium.TabIndex = 2;
            this.shader_button_medium.TabStop = true;
            this.shader_button_medium.Text = "Medium";
            this.shader_button_medium.UseVisualStyleBackColor = true;
            this.shader_button_medium.CheckedChanged += new System.EventHandler(this.shader_button_medium_CheckedChanged);
            // 
            // shader_button_low
            // 
            this.shader_button_low.AutoSize = true;
            this.shader_button_low.Font = new System.Drawing.Font("Arial Narrow", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.shader_button_low.Location = new System.Drawing.Point(36, 37);
            this.shader_button_low.Name = "shader_button_low";
            this.shader_button_low.Size = new System.Drawing.Size(51, 24);
            this.shader_button_low.TabIndex = 1;
            this.shader_button_low.TabStop = true;
            this.shader_button_low.Text = "Low";
            this.shader_button_low.UseVisualStyleBackColor = true;
            this.shader_button_low.CheckedChanged += new System.EventHandler(this.shader_button_low_CheckedChanged);
            // 
            // shader_label
            // 
            this.shader_label.AutoSize = true;
            this.shader_label.BackColor = System.Drawing.SystemColors.ControlLight;
            this.shader_label.Font = new System.Drawing.Font("Arial Narrow", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.shader_label.Location = new System.Drawing.Point(0, 0);
            this.shader_label.Name = "shader_label";
            this.shader_label.Size = new System.Drawing.Size(129, 25);
            this.shader_label.TabIndex = 0;
            this.shader_label.Text = "Shader Quality";
            // 
            // water_label
            // 
            this.water_label.AutoSize = true;
            this.water_label.BackColor = System.Drawing.SystemColors.ControlLight;
            this.water_label.Font = new System.Drawing.Font("Arial Narrow", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.water_label.Location = new System.Drawing.Point(5, 0);
            this.water_label.Name = "water_label";
            this.water_label.Size = new System.Drawing.Size(119, 25);
            this.water_label.TabIndex = 0;
            this.water_label.Text = "Water Quality";
            // 
            // water_panel
            // 
            this.water_panel.BackColor = System.Drawing.SystemColors.ControlLight;
            this.water_panel.Controls.Add(this.water_button_high);
            this.water_panel.Controls.Add(this.water_button_low);
            this.water_panel.Controls.Add(this.water_label);
            this.water_panel.Location = new System.Drawing.Point(26, 473);
            this.water_panel.Name = "water_panel";
            this.water_panel.Size = new System.Drawing.Size(129, 100);
            this.water_panel.TabIndex = 6;
            // 
            // water_button_high
            // 
            this.water_button_high.AutoSize = true;
            this.water_button_high.Font = new System.Drawing.Font("Arial Narrow", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.water_button_high.Location = new System.Drawing.Point(36, 67);
            this.water_button_high.Name = "water_button_high";
            this.water_button_high.Size = new System.Drawing.Size(54, 24);
            this.water_button_high.TabIndex = 3;
            this.water_button_high.TabStop = true;
            this.water_button_high.Text = "High";
            this.water_button_high.UseVisualStyleBackColor = true;
            this.water_button_high.CheckedChanged += new System.EventHandler(this.water_button_high_CheckedChanged);
            // 
            // water_button_low
            // 
            this.water_button_low.AutoSize = true;
            this.water_button_low.Font = new System.Drawing.Font("Arial Narrow", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.water_button_low.Location = new System.Drawing.Point(36, 37);
            this.water_button_low.Name = "water_button_low";
            this.water_button_low.Size = new System.Drawing.Size(51, 24);
            this.water_button_low.TabIndex = 1;
            this.water_button_low.TabStop = true;
            this.water_button_low.Text = "Low";
            this.water_button_low.UseVisualStyleBackColor = true;
            this.water_button_low.CheckedChanged += new System.EventHandler(this.water_button_low_CheckedChanged);
            // 
            // shadow_button_low
            // 
            this.shadow_button_low.AutoSize = true;
            this.shadow_button_low.Font = new System.Drawing.Font("Arial Narrow", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.shadow_button_low.Location = new System.Drawing.Point(36, 37);
            this.shadow_button_low.Name = "shadow_button_low";
            this.shadow_button_low.Size = new System.Drawing.Size(51, 24);
            this.shadow_button_low.TabIndex = 1;
            this.shadow_button_low.TabStop = true;
            this.shadow_button_low.Text = "Low";
            this.shadow_button_low.UseVisualStyleBackColor = true;
            this.shadow_button_low.CheckedChanged += new System.EventHandler(this.shadow_button_low_CheckedChanged);
            // 
            // shadow_label
            // 
            this.shadow_label.AutoSize = true;
            this.shadow_label.BackColor = System.Drawing.SystemColors.ControlLight;
            this.shadow_label.Font = new System.Drawing.Font("Arial Narrow", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.shadow_label.Location = new System.Drawing.Point(-4, 0);
            this.shadow_label.Name = "shadow_label";
            this.shadow_label.Size = new System.Drawing.Size(136, 25);
            this.shadow_label.TabIndex = 0;
            this.shadow_label.Text = "Shadow Quality";
            // 
            // shadow_panel
            // 
            this.shadow_panel.BackColor = System.Drawing.SystemColors.ControlLight;
            this.shadow_panel.Controls.Add(this.shadow_button_high);
            this.shadow_panel.Controls.Add(this.shadow_button_low);
            this.shadow_panel.Controls.Add(this.shadow_label);
            this.shadow_panel.Location = new System.Drawing.Point(161, 473);
            this.shadow_panel.Name = "shadow_panel";
            this.shadow_panel.Size = new System.Drawing.Size(129, 100);
            this.shadow_panel.TabIndex = 7;
            // 
            // shadow_button_high
            // 
            this.shadow_button_high.AutoSize = true;
            this.shadow_button_high.Font = new System.Drawing.Font("Arial Narrow", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.shadow_button_high.Location = new System.Drawing.Point(36, 67);
            this.shadow_button_high.Name = "shadow_button_high";
            this.shadow_button_high.Size = new System.Drawing.Size(54, 24);
            this.shadow_button_high.TabIndex = 3;
            this.shadow_button_high.TabStop = true;
            this.shadow_button_high.Text = "High";
            this.shadow_button_high.UseVisualStyleBackColor = true;
            this.shadow_button_high.CheckedChanged += new System.EventHandler(this.shadow_button_high_CheckedChanged);
            // 
            // vsync_label
            // 
            this.vsync_label.AutoSize = true;
            this.vsync_label.BackColor = System.Drawing.SystemColors.ControlLight;
            this.vsync_label.Font = new System.Drawing.Font("Arial Narrow", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.vsync_label.Location = new System.Drawing.Point(31, 0);
            this.vsync_label.Name = "vsync_label";
            this.vsync_label.Size = new System.Drawing.Size(60, 25);
            this.vsync_label.TabIndex = 0;
            this.vsync_label.Text = "Vsync";
            // 
            // vsync_panel
            // 
            this.vsync_panel.BackColor = System.Drawing.SystemColors.ControlLight;
            this.vsync_panel.Controls.Add(this.vsync_button_on);
            this.vsync_panel.Controls.Add(this.vsync_button_off);
            this.vsync_panel.Controls.Add(this.vsync_label);
            this.vsync_panel.Location = new System.Drawing.Point(296, 473);
            this.vsync_panel.Name = "vsync_panel";
            this.vsync_panel.Size = new System.Drawing.Size(129, 100);
            this.vsync_panel.TabIndex = 8;
            // 
            // vsync_button_on
            // 
            this.vsync_button_on.AutoSize = true;
            this.vsync_button_on.Font = new System.Drawing.Font("Arial Narrow", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.vsync_button_on.Location = new System.Drawing.Point(36, 67);
            this.vsync_button_on.Name = "vsync_button_on";
            this.vsync_button_on.Size = new System.Drawing.Size(44, 24);
            this.vsync_button_on.TabIndex = 3;
            this.vsync_button_on.TabStop = true;
            this.vsync_button_on.Text = "On";
            this.vsync_button_on.UseVisualStyleBackColor = true;
            this.vsync_button_on.CheckedChanged += new System.EventHandler(this.vsync_button_on_CheckedChanged);
            // 
            // vsync_button_off
            // 
            this.vsync_button_off.AutoSize = true;
            this.vsync_button_off.Font = new System.Drawing.Font("Arial Narrow", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.vsync_button_off.Location = new System.Drawing.Point(36, 37);
            this.vsync_button_off.Name = "vsync_button_off";
            this.vsync_button_off.Size = new System.Drawing.Size(43, 24);
            this.vsync_button_off.TabIndex = 1;
            this.vsync_button_off.TabStop = true;
            this.vsync_button_off.Text = "Off";
            this.vsync_button_off.UseVisualStyleBackColor = true;
            this.vsync_button_off.CheckedChanged += new System.EventHandler(this.vsync_button_off_CheckedChanged);
            // 
            // preset_label
            // 
            this.preset_label.AutoSize = true;
            this.preset_label.Font = new System.Drawing.Font("Arial Narrow", 12F);
            this.preset_label.Location = new System.Drawing.Point(203, 256);
            this.preset_label.Name = "preset_label";
            this.preset_label.Size = new System.Drawing.Size(48, 20);
            this.preset_label.TabIndex = 4;
            this.preset_label.Text = "Preset";
            // 
            // preset_combobox
            // 
            this.preset_combobox.FormattingEnabled = true;
            this.preset_combobox.Items.AddRange(new object[] {
            "None",
            "Low",
            "Medium",
            "High"});
            this.preset_combobox.Location = new System.Drawing.Point(166, 279);
            this.preset_combobox.Name = "preset_combobox";
            this.preset_combobox.Size = new System.Drawing.Size(121, 21);
            this.preset_combobox.TabIndex = 9;
            this.preset_combobox.SelectedIndexChanged += new System.EventHandler(this.preset_combobox_SelectedIndexChanged);
            // 
            // play_button
            // 
            this.play_button.BackColor = System.Drawing.Color.LightGray;
            this.play_button.Font = new System.Drawing.Font("Arial Narrow", 15.75F);
            this.play_button.Location = new System.Drawing.Point(26, 593);
            this.play_button.Name = "play_button";
            this.play_button.Size = new System.Drawing.Size(399, 97);
            this.play_button.TabIndex = 10;
            this.play_button.Text = "Play Game";
            this.play_button.UseVisualStyleBackColor = false;
            this.play_button.Click += new System.EventHandler(this.play_button_Click);
            // 
            // imageMain
            // 
            this.imageMain.Image = ((System.Drawing.Image)(resources.GetObject("imageMain.Image")));
            this.imageMain.Location = new System.Drawing.Point(103, 182);
            this.imageMain.Name = "imageMain";
            this.imageMain.Size = new System.Drawing.Size(251, 39);
            this.imageMain.TabIndex = 11;
            this.imageMain.TabStop = false;
            // 
            // pictureBox2
            // 
            this.pictureBox2.Image = ((System.Drawing.Image)(resources.GetObject("pictureBox2.Image")));
            this.pictureBox2.Location = new System.Drawing.Point(162, 46);
            this.pictureBox2.Name = "pictureBox2";
            this.pictureBox2.Size = new System.Drawing.Size(131, 130);
            this.pictureBox2.TabIndex = 13;
            this.pictureBox2.TabStop = false;
            // 
            // FormUnreal
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ControlLight;
            this.ClientSize = new System.Drawing.Size(453, 702);
            this.Controls.Add(this.pictureBox2);
            this.Controls.Add(this.imageMain);
            this.Controls.Add(this.play_button);
            this.Controls.Add(this.preset_combobox);
            this.Controls.Add(this.preset_label);
            this.Controls.Add(this.water_panel);
            this.Controls.Add(this.shader_panel);
            this.Controls.Add(this.shadow_panel);
            this.Controls.Add(this.vsync_panel);
            this.Controls.Add(this.texture_panel);
            this.Controls.Add(this.model_panel);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MaximizeBox = false;
            this.Name = "FormUnreal";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Unreal Half Life";
            this.Load += new System.EventHandler(this.FormUnreal_Load);
            this.model_panel.ResumeLayout(false);
            this.model_panel.PerformLayout();
            this.texture_panel.ResumeLayout(false);
            this.texture_panel.PerformLayout();
            this.shader_panel.ResumeLayout(false);
            this.shader_panel.PerformLayout();
            this.water_panel.ResumeLayout(false);
            this.water_panel.PerformLayout();
            this.shadow_panel.ResumeLayout(false);
            this.shadow_panel.PerformLayout();
            this.vsync_panel.ResumeLayout(false);
            this.vsync_panel.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.imageMain)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Panel model_panel;
        private System.Windows.Forms.RadioButton model_button_high;
        private System.Windows.Forms.RadioButton model_button_medium;
        private System.Windows.Forms.RadioButton model_button_low;
        private System.Windows.Forms.Label model_label;
        private System.Windows.Forms.RadioButton texture_button_high;
        private System.Windows.Forms.RadioButton texture_button_medium;
        private System.Windows.Forms.RadioButton texture_button_low;
        private System.Windows.Forms.Label texture_label;
        private System.Windows.Forms.Panel texture_panel;
        private System.Windows.Forms.Panel shader_panel;
        private System.Windows.Forms.RadioButton shader_button_high;
        private System.Windows.Forms.RadioButton shader_button_medium;
        private System.Windows.Forms.RadioButton shader_button_low;
        private System.Windows.Forms.Label shader_label;
        private System.Windows.Forms.Label water_label;
        private System.Windows.Forms.Panel water_panel;
        private System.Windows.Forms.RadioButton water_button_high;
        private System.Windows.Forms.RadioButton water_button_low;
        private System.Windows.Forms.RadioButton shadow_button_low;
        private System.Windows.Forms.Label shadow_label;
        private System.Windows.Forms.Panel shadow_panel;
        private System.Windows.Forms.RadioButton shadow_button_high;
        private System.Windows.Forms.Label vsync_label;
        private System.Windows.Forms.Panel vsync_panel;
        private System.Windows.Forms.RadioButton vsync_button_on;
        private System.Windows.Forms.RadioButton vsync_button_off;
        private System.Windows.Forms.Label preset_label;
        private System.Windows.Forms.ComboBox preset_combobox;
        private System.Windows.Forms.Button play_button;
        private System.Windows.Forms.PictureBox imageMain;
        private System.Windows.Forms.PictureBox pictureBox2;
    }
}

